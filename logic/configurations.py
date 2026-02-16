import os
import ansible_runner
import yaml
import glob
import sys
import ipaddress


from termcolor import cprint

class Configurations:
    """Gestion des configurations"""
    def __init__(self, projectFolder, data):
        self.devices = []  # List of devices with their details
        self.projectFolder = projectFolder
        self.data = data
        self.load_devices()

    def load_devices(self):
        """Load devices from host_vars YAML files."""
        # Check standard locations for host_vars
        host_vars_dir = os.path.join(self.projectFolder, "host_vars")
        if not os.path.exists(host_vars_dir):
            host_vars_dir = os.path.join(self.projectFolder, "yaml_files", "host_vars")
            if not os.path.exists(host_vars_dir):
                print(f"No host_vars found in {self.projectFolder}")
                return

        yaml_files = glob.glob(os.path.join(host_vars_dir, "*.yml"))
        for yaml_file in yaml_files:
            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    data = dict(yaml.safe_load(f))
                    cprint("Data", 'light_yellow')
                    print(data)
                    if data:
                        # Extract hostname from 
                        hostname = data['hostname']
                        # hostname = os.path.splitext(os.path.basename(yaml_file))[0]
                        # Ensure device type exists
                        if data:
                            self.devices.append({
                                'hostname': hostname,
                                'constructor': data['ansible_network_os'],
                                'device_type': data['device_type'].lower(), # 'router', 'switch', 'pc'
                                'variables': data,
                                'filename': yaml_file
                            })
            except Exception as e:
                print(f"Error loading {yaml_file}: {e}")

    def generate_configurations(self, status_callback=None, progress_callback=None):
        """Generate configurations with Ansible"""
        if not self.devices:
            print("No devices to configure.")
            return

        # Locate ansible_files directory relative to the codebase root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        playbook_path = os.path.join(base_dir, "ansible_files", "playbook.yml")
        
        output_dir = os.path.join(self.projectFolder, "configurations")
        os.makedirs(output_dir, exist_ok=True)

        if status_callback:
            status_callback("Building inventory...")

        # Prepare host_vars directory
        host_vars_dir = os.path.join(self.projectFolder, "host_vars")
        os.makedirs(host_vars_dir, exist_ok=True)
        
        # Prepare group names
        groups = set([f'{group_name["device_type"]}s' for group_name in self.devices])
        print(groups)

        # Inventory blue print
        hosts = {}
        for group in groups:
            hosts[group] = []

        for device in self.devices:
            hostname = device['hostname']
            device_type = device.get('device_type', 'ungrouped')
            device_group = f'{device_type}s'

            if device_group in hosts.keys():
                hosts[device_group].append(hostname)
                
            # Prepare host variables
            host_vars = device['variables'].copy()
            host_vars['device_type'] = device_type
            host_vars['currentProjectPath'] = self.projectFolder
            
            # Standardize 'interfaces' to be a list of dictionaries with 'name' attribute
            # This ensures compatibility with all templates (router.j2, switch.j2, pc.j2)
            if 'interfaces' in host_vars and isinstance(host_vars['interfaces'], dict):
                interfaces_list = []
                for if_name, if_data in host_vars['interfaces'].items():
                    if isinstance(if_data, dict):
                        # Create a new dict to avoid modifying the original reference if shared
                        new_if_data = if_data.copy()
                        new_if_data['name'] = if_name
                        interfaces_list.append(new_if_data)
                    else:
                        # Handle case where val might not be dict (unlikely based on topology_data)
                        interfaces_list.append({'name': if_name})
                host_vars['interfaces'] = interfaces_list
            elif 'interfaces' not in host_vars:
                host_vars['interfaces'] = []

            # Special handling for PCs: ensure robust IP handling
            if device_type == 'pc':
                # If we have legacy 'ip' at root, ensure it's in an interface
                ip_cidr = host_vars.get('ip')
                
                # Check if we already have an interface with IP
                has_ip_interface = False
                for iface in host_vars['interfaces']:
                    if 'ip' in iface or 'address' in iface:
                        has_ip_interface = True
                        break
                
                if not has_ip_interface and ip_cidr:
                    # Create default eth0 interface
                    try:
                        iface_obj = ipaddress.ip_interface(ip_cidr)
                        host_vars['interfaces'].append({
                            'name': 'eth0',
                            'address': str(iface_obj.ip),
                            'netmask': str(iface_obj.netmask),
                            'ip': ip_cidr # Keep raw cidr just in case
                        })
                    except ValueError as e:
                        print(f"Error parsing IP for {hostname}: {e}")
                        host_vars['interfaces'].append({
                            'name': 'eth0',
                            'ip': ip_cidr
                        })
            
            # Write host_vars to file
            host_var_path = os.path.join(host_vars_dir, f"{hostname}.yml")
            with open(host_var_path, 'w') as f:
                yaml.dump(host_vars, f, default_flow_style=False)

        # Save the inventory to ini file

        inventory_path = os.path.join(self.projectFolder, "inventory.ini")
        with open(inventory_path, 'w') as f:
            for group, hosts in hosts.items():
                f.write(f"[{group}]\n") # Group name
                for host in hosts:
                    f.write(f"{host}\n")    # Hostname
                f.write("\n")

        print(f"Inventory saved to {inventory_path}")
        print(f"Host variables saved to {host_vars_dir}")

        print(f"Generating configurations using playbook: {playbook_path}")
        
        if status_callback:
            status_callback("Running Ansible Playbook...")

        total_hosts = len(self.devices)
        completed_hosts = 0

        def event_handler(event):
            nonlocal completed_hosts
            # event is a dict. 'event' key tells the type.
            # We look for successful template generation.
            # 'runner_on_ok' happens when a task finishes for a host.
            # The task name is "GENERATE CONFIGS FOR EACH OS"
            if event.get('event') == 'runner_on_ok':
                event_data = event.get('event_data', {})
                task_name = event_data.get('task', '')
                if "GENERATE CONFIGS" in task_name:
                    completed_hosts += 1
                    if progress_callback:
                        # Calculate percentage
                        # We might have other overhead, so let's scale it.
                        # Simple: (completed / total) * 100
                        percent = int((completed_hosts / total_hosts) * 100)
                        progress_callback(percent)

        # Run Ansible Runner
        # We pass the inventory path so Ansible mimics CLI behavior and finds host_vars/

        # Execute the Ansible playbook using ansible_runner to generate configurations.
        # - private_data_dir: The root directory for Ansible execution context.
        # - playbook: The path to the specific playbook to run.
        # - inventory: The path to the generated inventory file.
        # - quiet: If False, Ansible output is printed to stdout.
        # - event_handler: A callback function used here to track task completion and update progress.
        r = ansible_runner.run(
            private_data_dir=base_dir,
            playbook=playbook_path,
            inventory=inventory_path,
            extravars={'currentProjectPath': self.projectFolder},
            quiet=False,
            event_handler=event_handler
        )
        
        if r.status == 'successful':
             print(f"Configurations generated successfully in {output_dir}")
        else:
             print("Error generating configurations")
             print(r.stdout.read())
    
    def apply_configurations(self):
        """Apply configurations to the network"""
        pass

    def get_equipment_config_file(self, projectFolder, equipmentName):
        """Charge le fichier de configuration d'un equipement"""
        configFile = os.path.join(projectFolder, "configurations", f"{equipmentName}.cfg")
        if not os.path.exists(configFile):
            return False
        return configFile