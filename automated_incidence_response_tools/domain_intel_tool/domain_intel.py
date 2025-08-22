import socket
import whois
import requests
import json
import argparse

VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY"  # Replace or use env var
ABUSEIPDB_API_KEY = "YOUR_ABUSEIPDB_API_KEY"  # Optional

def get_whois_info(domain):
    try:
        return whois.whois(domain)
    except Exception as e:
        return {"error": str(e)}

def get_dns_records(domain):
    try:
        return {
            "A": socket.gethostbyname(domain),
            "MX": socket.getaddrinfo(domain, 25),
            "NS": socket.getaddrinfo(domain, 53),
        }
    except Exception as e:
        return {"error": str(e)}

def get_reverse_ip(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return {"host": result[0], "aliases": result[1]}
    except Exception as e:
        return {"error": str(e)}

def check_virustotal(domain_or_ip):
    url = f"https://www.virustotal.com/api/v3/domains/{domain_or_ip}"
    headers = {"x-apikey": VT_API_KEY}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return {
            "reputation": data.get("data", {}).get("attributes", {}).get("reputation", "N/A"),
            "categories": data.get("data", {}).get("attributes", {}).get("categories", {}),
            "last_analysis_stats": data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        }
    except Exception as e:
        return {"error": str(e)}

def check_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": ABUSEIPDB_API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip}
    try:
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Domain & IP Intelligence Tool")
    parser.add_argument("target", help="Domain or IP address to investigate")
    parser.add_argument("--output", help="Save result to JSON file", default=None)
    args = parser.parse_args()

    target = args.target
    result = {}

    print(f"\n🔍 Investigating: {target}")

    # WHOIS
    print("➤ Fetching WHOIS...")
    result["whois"] = str(get_whois_info(target))

    # DNS Records
    print("➤ Fetching DNS records...")
    result["dns"] = get_dns_records(target)

    # IP Detection
    try:
        ip = socket.gethostbyname(target)
    except:
        ip = target  # Assume it's already an IP

    # Reverse IP
    print("➤ Reverse IP lookup...")
    result["reverse_ip"] = get_reverse_ip(ip)

    # VirusTotal
    print("➤ Checking VirusTotal...")
    result["virustotal"] = check_virustotal(target)

    # AbuseIPDB
    print("➤ Checking AbuseIPDB...")
    result["abuseipdb"] = check_abuseipdb(ip)

    print("\n✅ Summary:")
    print(json.dumps(result, indent=2))

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\n📁 Saved output to {args.output}")

if __name__ == "__main__":
    main()
