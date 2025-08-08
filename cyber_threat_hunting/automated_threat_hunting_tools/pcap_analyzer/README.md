# 📡 PCAP Analyzer — Network Threat Detector

Analyzes `.pcap` files to detect:
- Suspicious ports (used in malware, reverse shells, RATs)
- Protocol usage (ICMP, TCP, DNS)
- Most active IPs
- Basic signs of C2 or scanning behavior

## 🔧 Usage

```bash
python analyze_pcap.py sample.pcap --output report.json
