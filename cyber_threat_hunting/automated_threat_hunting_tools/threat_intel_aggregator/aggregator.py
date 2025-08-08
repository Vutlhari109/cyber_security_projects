import requests

# Optional API keys (set if available)
ABUSEIPDB_API_KEY = "your_abuseipdb_api_key"
ALIENVAULT_API_KEY = "your_alienvault_api_key"  # Optional, for OTX

def get_abuseipdb_reports(ip):
    if not ABUSEIPDB_API_KEY or ABUSEIPDB_API_KEY == "your_abuseipdb_api_key":
        print("[-] No AbuseIPDB API key provided.")
        return

    url = f"https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()["data"]
        print(f"[AbuseIPDB] IP: {ip}")
        print(f"  Abuse Score: {data['abuseConfidenceScore']}")
        print(f"  Total Reports: {data['totalReports']}")
        print(f"  Country: {data['countryCode']}")
    else:
        print(f"[-] AbuseIPDB error: {response.status_code}")

def get_otx_data(ioc):
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ioc}/general"
    headers = {
        "X-OTX-API-KEY": ALIENVAULT_API_KEY
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"[OTX] Indicator: {ioc}")
        print(f"  Pulses: {len(data.get('pulse_info', {}).get('pulses', []))}")
        print(f"  Malware Families: {data.get('malware_families')}")
    else:
        print(f"[-] OTX error for {ioc}: {response.status_code}")

if __name__ == "__main__":
    ioc = input("Enter IP address or IOC to check: ").strip()
    get_abuseipdb_reports(ioc)
    get_otx_data(ioc)
