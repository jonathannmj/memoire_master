import re

class TopologyDataStub:
    def normalise_interfaces_names(self, text):
        """
        Convertit les abréviations en noms complets d'interfaces réseau.
        Supporte: f0/0, gi0/0, s0/0, eth0, etc.
        Gère également les erreurs OCR où '0' est lu comme 'o' ou 'O'.
        """
        substitutions = {
            r'(?i)^(?:GigabitEthernet|Gig|Gi|g)([\doO]+(?:/[\doO]+){1,2})$': r'GigabitEthernet\1',
            r'(?i)^(?:FastEthernet|FastEth|Fa|fo|f)([\doO]+(?:/[\doO]+){1,2})$': r'FastEthernet\1',
            r'(?i)^(?:TenGigabitEthernet|TenGig|Te)([\doO]+(?:/[\doO]+){1,2})$': r'TenGigabitEthernet\1',
            r'(?i)^(?:Ethernet|Eth|e)([\doO]+(?:/[\doO]+){0,2})$': r'Ethernet\1',
            r'(?i)^(?:Serial|Se|s)([\doO]+(?:/[\doO]+){1,3})$': r'Serial\1',
            r'(?i)^(?:Loopback|Lo)([\doO]+)$': r'Loopback\1',
            r'(?i)^(?:Vlan|Vl|v)([\doO]+)$': r'Vlan\1',
            r'(?i)^(?:Port-channel|Po)([\doO]+)$': r'Port-channel\1',
        }

        for pattern, replacement in substitutions.items():
            match = re.match(pattern, text)
            if match:
                numeric_part = match.group(1)
                cleaned_numeric = numeric_part.replace('o', '0').replace('O', '0')
                prefix = replacement.replace(r'\1', '')
                return prefix + cleaned_numeric
        return text

td = TopologyDataStub()

# Test cases
cases = [
    ("fo/0", "FastEthernet0/0"),
    ("go/0", "GigabitEthernet0/0"),
    ("LoO", "Loopback0"), # LoopbackO -> Loopback0
    ("f0/o", "FastEthernet0/0"), # f0/o -> FastEthernet0/0
    ("eO/O", "Ethernet0/0"),
    ("s0/0/0", "Serial0/0/0"), # Standard case
]

for inp, expected in cases:
    res = td.normalise_interfaces_names(inp)
    print(f"'{inp}' -> '{res}' | Expected: '{expected}' | Match: {res == expected}")
    if res != expected:
        print("FAILED")

