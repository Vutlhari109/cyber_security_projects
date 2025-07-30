import socket

def port_scan(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        print(f"Port {port} on {ip} is OPEN")
        s.close()
    except:
        print(f"Port {port} on {ip} is CLOSED")

# Run the scan on a known IP and port
port_scan("10.236.245.104", 53)
     