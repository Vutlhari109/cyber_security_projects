# Scenario 3: DNS Spoofing with Local Response

## Description
A client `192.168.50.10` queries Google DNS `8.8.8.8` for `www.bank.com`.

## Key Observations
- The DNS response comes not from the trusted server `8.8.8.8`, but from a local IP `192.168.50.200`.
- The fake response returns IP `192.168.50.250` instead of the real IP.
- This indicates DNS spoofing or poisoning inside the local network.

## Explanation
- Even if `192.168.50.200` is the real server, receiving the reply from an unexpected IP breaks trust.
- The client might be redirected or intercepted due to this spoofing.

## Conclusion
Watch for DNS responses coming from unexpected sources; this is a key sign of network attacks.
