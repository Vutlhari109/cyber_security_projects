# 🌐 Domain Recon Scanner (Flask)

This is a **lightweight domain reconnaissance tool** built with Flask. It performs quick scans using:

- `nmap` (Fast port scan)
- `whois` (Domain registration info)
- `nslookup` (DNS resolution)

---

## 🚀 Features

- 🖥️ Web-based Flask API endpoint
- 📜 Auto logs all scans to `scan_logs.txt`
- 📄 Returns structured HTML output for better readability (optional CSS-friendly)
- ⚠️ Safe subprocess calls (no shell injection)

---

## 🛠️ Requirements

- Python 3.8+
- Linux/macOS with `nmap`, `whois`, and `nslookup` installed

```bash
sudo apt install nmap whois dnsutils -y
