import pyshark
import argparse
from collections import Counter
import json

# Define suspicious ports (commonly used in malware, reverse shells, RATs, etc.)
SUSPICIOUS_PORTS = {1337, 4444, 6667, 3389, 23, 8080}

def analyze_pcap(file_path):
    cap = pyshark.FileCapture(file_path, only_summaries=True)
    
    port_counter = Counter()
    ip_counter = Counter()
    protocol_counter = Counter()
    alerts = []

    print(f"\n📄 Analyzing PCAP: {file_path}")

    for pkt in cap:
        try:
            info = pkt.info.lower()
            src, dst = pkt.source, pkt.destination
            proto = pkt.protocol.lower()
            port_info = pkt.info

            protocol_counter[proto] += 1
            ip_counter[src] += 1

            # Detect port from summary (basic heuristic)
            for port in SUSPICIOUS_PORTS:
                if str(port) in port_info:
                    alerts.append(f"⚠️ Suspicious port {port} used in: {info}")
                    port_counter[port] += 1

        except Exception as e:
            continue

    result = {
        "most_active_ips": ip_counter.most_common(5),
        "most_used_protocols": protocol_counter.most_common(5),
        "suspicious_ports_found": dict(port_counter),
        "alerts": alerts
    }

    return result

def main():
    parser = argparse.ArgumentParser(description="PCAP Threat Analyzer")
    parser.add_argument("file", help="Path to the .pcap file")
    parser.add_argument("--output", help="Save output as JSON", default=None)
    args = parser.parse_args()

    result = analyze_pcap(args.file)

    print("\n✅ Summary:")
    print(json.dumps(result, indent=2))

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\n📁 Saved results to {args.output}")

if __name__ == "__main__":
    main()
