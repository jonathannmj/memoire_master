import sys
import os

# Add the project root to sys.path so we can import Classes
project_root = "/home/jonathan/Documents/master2/memoire/codes_memoire"
sys.path.append(project_root)

from Classes.configurations import Configurations

def main():
    # Path to yaml_files directory which contains host_vars
    # In the real app, this is passed as the project path.
    # Based on list_dir, yaml_files is in codes_memoire. 
    # But Configurations logic looks for host_vars inside the projectFolder OR inside projectFolder/yaml_files.
    # Let's pass the root codes_memoire as the project folder.
    project_folder = project_root
    
    print(f"Initializing Configurations with project folder: {project_folder}")
    configs = Configurations(project_folder)
    
    print(f"Found {len(configs.devices)} devices.")
    for dev in configs.devices:
        print(f" - {dev['name']} ({dev['constructor']})")
        
    print("\nStarting generation...")
    configs.generate_configurations()
    
    print("\nChecking for generated configurations...")
    output_dir = os.path.join(project_folder, "configurations")
    if os.path.exists(output_dir):
        files = os.listdir(output_dir)
        print(f"Files in {output_dir}: {files}")
        
        # Print content of one file if exists
        for f in files:
            if f.endswith(".cfg"):
                print(f"\nContent of {f}:")
                with open(os.path.join(output_dir, f), 'r') as cfg:
                    print(cfg.read())
                break
    else:
        print(f"Output directory {output_dir} does not exist.")

if __name__ == "__main__":
    main()
