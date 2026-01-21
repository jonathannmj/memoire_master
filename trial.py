from Classes.topology_data import TopologyData


def test_save_data_to_yaml():
    data = {'nodes': {'pc_1': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': 'pc', 'ip': '192.168.1.1/24'}, 'gateway_2': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': 'gateway', 'interfaces': {}}, 'pc_3': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': 'pc', 'ip': '192.168.1.1/24'}, 'pc_4': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': 'pc', 'ip': '192.168.1.1/24'}, 'KaliLinux-1': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': 'pc', 'ip': '192.168.1.1/24'}, 'router_6': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': 'router', 'interfaces': {}}, 'cloud_7': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': 'cloud', 'interfaces': {}}, '{}_8': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': {}, 'interfaces': {}}, '{}_9': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': {}, 'interfaces': {}}, 'pc_10': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': 'pc', 'ip': '192.168.1.1/24'}, 'server_11': {'ansible_connection': 'network_cli', 'ansible_user': '<USERNAME>', 'ansible_network_os': 'ios', 'device': 'server', 'interfaces': {}}}}

    TopologyData.save_data_to_yaml(data, 'yaml_files')

    print("Done")

test_save_data_to_yaml()