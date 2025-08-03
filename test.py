# Send Requests to Server.py for Checking 
import sys

if len(sys.argv) < 4:
    print("Usage: python3 script.py <address> <port> <domain>")
    sys.exit(1)

address = sys.argv[1]
port = sys.argv[2]
domain = sys.argv[3]

print(f"[+] Received inputs:")
print(f"    - Address: {address}")
print(f"    - Port: {port}")
print(f"    - Domain: {domain}")