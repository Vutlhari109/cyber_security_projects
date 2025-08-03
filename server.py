from flask import Flask, request, jsonify
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    domain = request.form.get("target")
    if not domain:
        return jsonify({"error": "Missing target"}), 400

    nmap = subprocess.run(["nmap", "-F", domain], capture_output=True, text=True).stdout
    whois = subprocess.run(["whois", domain], capture_output=True, text=True).stdout
    nslookup = subprocess.run(["nslookup", domain], capture_output=True, text=True).stdout

    # Log every scan
    with open("scan_logs.txt", "a") as f:
        f.write(f"{datetime.now()} - Scan: {domain}\n")

    return jsonify({
        "nmap": nmap,
        "whois": whois,
        "nslookup": nslookup
    })

if __name__ == "__main__":
    app.run(port=5000)