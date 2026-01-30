import re

class TopologyDataStub:
    def normalise_interfaces_names(self, text):
        """
        Convertit les abréviations en noms complets d'interfaces réseau.
        Supporte: f0/0, gi0/0, s0/0, eth0, etc.
        """
        substitutions = {
            r'(?i)^(?:GigabitEthernet|Gig|Gi|g)(\d+(?:/\d+){1,2})$': r'GigabitEthernet\1',
            r'(?i)^(?:FastEthernet|FastEth|Fa|fo|f)(\d+(?:/\d+){1,2})$': r'FastEthernet\1',
            r'(?i)^(?:TenGigabitEthernet|TenGig|Te)(\d+(?:/\d+){1,2})$': r'TenGigabitEthernet\1',
            r'(?i)^(?:Ethernet|Eth|e)(\d+(?:/\d+){0,2})$': r'Ethernet\1',
            r'(?i)^(?:Serial|Se|s)(\d+(?:/\d+){1,3})$': r'Serial\1',
            r'(?i)^(?:Loopback|Lo)(\d+)$': r'Loopback\1',
            r'(?i)^(?:Vlan|Vl|v)(\d+)$': r'Vlan\1',
            r'(?i)^(?:Port-channel|Po)(\d+)$': r'Port-channel\1',
        }

        for pattern, replacement in substitutions.items():
            if re.match(pattern, text):
                return re.sub(pattern, replacement, text)
        return text

td = TopologyDataStub()

print(f"Testing 'fo/0' -> {td.normalise_interfaces_names('fo/0')}")
assert td.normalise_interfaces_names('fo/0') == 'FastEthernet0/0'
print("SUCCESS: 'fo/0' is handled correctly.")
