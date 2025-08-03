from flask import Flask, request, jsonify
import subprocess
import re

app = Flask(__name__)

def is_valid_domain(domain):
    # Basic domain format check
    return bool(re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain))

@app.route('/scan', methods=['POST'])
def scan():
    domain = request.form.get("target")

    if not domain:
        return jsonify({"error": "Missing target"}), 400

    if not is_valid_domain(domain):
        return jsonify({"error": "Invalid domain format"}), 400

    try:
        nmap_result = subprocess.run(
            ["nmap", "-F", domain], capture_output=True, text=True, timeout=10
        ).stdout

        whois_result = subprocess.run(
            ["whois", domain], capture_output=True, text=True, timeout=10
        ).stdout

        nslookup_result = subprocess.run(
            ["nslookup", domain], capture_output=True, text=True, timeout=10
        ).stdout

        return jsonify({
            "nmap": nmap_result.strip(),
            "whois": whois_result.strip(),
            "nslookup": nslookup_result.strip()
        })

    except subprocess.TimeoutExpired:
        return jsonify({"error": "One of the tools timed out"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(port=5000)