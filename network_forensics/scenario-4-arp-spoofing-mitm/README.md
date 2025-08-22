# Scenario 4: ARP Spoofing / Man-in-the-Middle Attack

## Description
This capture shows an ARP request for the gateway `192.168.1.1` from `192.168.1.100`.

## Key Observations
- The legitimate gateway responds with its real MAC address `00:11:22:33:44:55`.
- Multiple subsequent replies claim the same IP `192.168.1.1` but with a different MAC `66:77:88:99:AA:BB`.
- This indicates an attacker trying to impersonate the gateway.

## Why Suspicious?
- ARP spoofing can redirect traffic through the attacker’s machine.
- Enables man-in-the-middle attacks, eavesdropping, or traffic modification.

## Conclusion
Multiple conflicting ARP replies for the same IP indicate a possible MitM attack via ARP poisoning.
