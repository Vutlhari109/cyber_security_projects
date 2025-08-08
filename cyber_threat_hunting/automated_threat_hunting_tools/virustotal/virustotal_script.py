import requests
import datetime
import os

API_KEY = "8621ddc2190eb12b39a1c753c2f94ec5da2709a74f4940ff3a699359ccd176ac"
HEADERS = {"x-apikey": API_KEY}

# List of IOCs (domains or IPs)
iocs = ["example.com", "google.com", "185.220.101.34", "suspicious-domain.xyz"]

VT_DOMAIN_URL = "https://www.virustotal.com/api/v3/domains/{}"
VT_IP_URL = "https://www.virustotal.com/api/v3/ip_addresses/{}"

def is_ip(ioc):
    return all(part.isdigit() and 0 <= int(part) <= 255 for part in ioc.split("."))

def get_virustotal_report(ioc):
    url = VT_IP_URL.format(ioc) if is_ip(ioc) else VT_DOMAIN_URL.format(ioc)
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        return {
            "ioc": ioc,
            "status": "Error",
            "detections": "N/A",
            "engines": [],
            "error": response.text
        }

    data = response.json()
    try:
        attributes = data["data"]["attributes"]
        stats = attributes["last_analysis_stats"]
        results = attributes["last_analysis_results"]

        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)
        harmless = stats.get("harmless", 0)
        undetected = stats.get("undetected", 0)
        total = sum(stats.values())

        detection_ratio = f"{malicious + suspicious}/{total}"
        
        if malicious > 0:
            status = "Malicious"
        elif suspicious > 0:
            status = "Suspicious"
        else:
            status = "Clean"

        # Collect detecting engines
        engines = [engine for engine, result in results.items() if result["category"] in ["malicious", "suspicious"]]

        # Optional: Save full JSON per IOC
        with open(f"raw_reports/{ioc.replace('.', '_')}.json", "w") as f:
            f.write(response.text)

        return {
            "ioc": ioc,
            "status": status,
            "detections": detection_ratio,
            "engines": engines,
            "error": None
        }
    except KeyError:
        return {
            "ioc": ioc,
            "status": "Parsing Error",
            "detections": "N/A",
            "engines": [],
            "error": "KeyError"
        }

# Ensure folder exists
os.makedirs("raw_reports", exist_ok=True)

# Create Markdown Report
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("threat_report.md", "w") as report:
    report.write(f"# Threat Hunting Report\nGenerated: {timestamp}\n\n")
    for ioc in iocs:
        result = get_virustotal_report(ioc)
        report.write(f"## {result['ioc']}\n")
        report.write(f"- Status: {result['status']}\n")
        report.write(f"- Detections: {result['detections']}\n")
        if result["engines"]:
            report.write(f"- Detected by: {', '.join(result['engines'])}\n")
        if result["error"]:
            report.write(f"- Error: {result['error']}\n")
        report.write("\n")

print("✅ Report generated: threat_report.md")

