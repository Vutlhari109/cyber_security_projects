# Scenario 1: DNS Spoofing (Fake DNS Reply)

## Description
This capture shows a DNS request from a client (`192.168.1.50`) to Google DNS (`8.8.8.8`) asking for the IP address of `www.paypal.com`.

## Key Points
- The three-way TCP handshake with `8.8.8.8` completes successfully.
- The client sends a DNS query for `www.paypal.com`.
- The DNS response comes *not* from the trusted DNS server (`8.8.8.8`) but from a local IP `192.168.1.200`.
- The fake DNS server responds with an IP `192.168.1.250`, likely a malicious or spoofed address.

## Why Suspicious?
- DNS responses should come from the queried DNS server.
- Receiving DNS replies from an unexpected local IP indicates DNS spoofing or poisoning.
- This can redirect users to malicious sites or intercept traffic.

## Conclusion
This pattern suggests a DNS spoofing attack inside the local network and should be investigated immediately.
