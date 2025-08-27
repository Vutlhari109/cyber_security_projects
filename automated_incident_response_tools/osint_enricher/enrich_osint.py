import requests
import argparse
import json

VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY"  # Optional
HIBP_API_KEY = "YOUR_HIBP_API_KEY"      # Optional (can skip breach check)

def check_hibp(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": HIBP_API_KEY,
        "user-agent": "threat-hunting-tool"
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 404:
            return {"breached": False}
        elif r.status_code == 200:
            return {"breached": True, "details": r.json()}
        else:
            return {"error": f"Status {r.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def check_virustotal_domain(domain):
    headers = {"x-apikey": VT_API_KEY}
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    try:
        r = requests.get(url, headers=headers)
        data = r.json()
        return {
            "reputation": data["data"]["attributes"]["reputation"],
            "categories": data["data"]["attributes"].get("categories", {}),
            "last_analysis_stats": data["data"]["attributes"]["last_analysis_stats"]
        }
    except Exception as e:
        return {"error": str(e)}

def username_osint(username):
    platforms = [
        f"https://github.com/{username}",
        f"https://twitter.com/{username}",
        f"https://reddit.com/u/{username}",
        f"https://www.instagram.com/{username}/",
    ]
    results = {}
    for url in platforms:
        try:
            response = requests.get(url)
            results[url] = "✅ Found" if response.status_code == 200 else "❌ Not Found"
        except:
            results[url] = "Error"
    return results

def main():
    parser = argparse.ArgumentParser(description="OSINT Enricher Tool")
    parser.add_argument("--email", help="Email address to check breaches")
    parser.add_argument("--domain", help="Domain to check reputation")
    parser.add_argument("--username", help="Username to check social presence")
    parser.add_argument("--output", help="Save result to JSON", default=None)
    args = parser.parse_args()

    result = {}

    if args.email:
        print(f"🔍 Checking breaches for {args.email}...")
        result["hibp"] = check_hibp(args.email)

    if args.domain:
        print(f"🔍 Checking VirusTotal for {args.domain}...")
        result["virustotal"] = check_virustotal_domain(args.domain)

    if args.username:
        print(f"🔍 Searching username {args.username} across platforms...")
        result["user_osint"] = username_osint(args.username)

    print("\n✅ OSINT Report:")
    print(json.dumps(result, indent=2))

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\n📁 Results saved to {args.output}")

if __name__ == "__main__":
    main()
