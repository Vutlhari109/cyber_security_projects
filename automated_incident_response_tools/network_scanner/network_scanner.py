from flask import Flask, request, jsonify
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    domain = request.form.get("target")
    if not domain:
        return jsonify({"error": "Missing target"}), 400

    # Run commands
    try:
        nmap = subprocess.run(["nmap", "-F", domain], capture_output=True, text=True, timeout=2000).stdout
        whois = subprocess.run(["whois", domain], capture_output=True, text=True, timeout=20000).stdout
        nslookup = subprocess.run(["nslookup", domain], capture_output=True, text=True, timeout=2000).stdout
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Command timed out"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Log scan with timestamp and results
    with open("logs/scan_logs.txt", "a") as f:
        f.write(f"\n\n=== Scan: {domain} | {datetime.now()} ===\n")
        f.write(f"\n[NMAP]\n{nmap}")
        f.write(f"\n[WHOIS]\n{whois}")
        f.write(f"\n[NSLOOKUP]\n{nslookup}")
        f.write("=" * 40 + "\n")

    return jsonify({
        "nmap": nmap,
        "whois": whois,
        "nslookup": nslookup
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
