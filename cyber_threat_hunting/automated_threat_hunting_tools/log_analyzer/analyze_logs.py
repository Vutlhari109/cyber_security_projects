import re
import argparse
from collections import Counter
import json

# Define suspicious keywords or paths
SUSPICIOUS_PATHS = ["/admin", "/login", "/wp-login.php", "/phpmyadmin", "/.env"]

# Regex pattern for Apache/Nginx logs (Common Log Format)
LOG_PATTERN = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(.*?)\] "(?P<method>GET|POST|HEAD|PUT|DELETE|OPTIONS) (?P<path>.*?) HTTP/\d\.\d" (?P<status>\d{3})'
)

def analyze_log_file(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    ip_counter = Counter()
    suspicious_requests = []
    brute_force_attempts = Counter()
    suspicious_path_hits = Counter()

    for line in lines:
        match = LOG_PATTERN.search(line)
        if match:
            ip = match.group("ip")
            path = match.group("path")
            status = int(match.group("status"))

            ip_counter[ip] += 1

            # Brute-force: many 401 or 403
            if status in [401, 403]:
                brute_force_attempts[ip] += 1

            # Suspicious paths
            for suspicious_path in SUSPICIOUS_PATHS:
                if suspicious_path in path:
                    suspicious_requests.append(f"{ip} accessed {path}")
                    suspicious_path_hits[path] += 1

    result = {
        "top_ips": ip_counter.most_common(5),
        "brute_force_ips": brute_force_attempts.most_common(5),
        "suspicious_path_hits": dict(suspicious_path_hits),
        "suspicious_requests": suspicious_requests,
    }

    return result

def main():
    parser = argparse.ArgumentParser(description="Log File Analyzer")
    parser.add_argument("logfile", help="Path to log file (Apache/Nginx)")
    parser.add_argument("--output", help="Save result to JSON", default=None)
    args = parser.parse_args()

    result = analyze_log_file(args.logfile)

    print("\n✅ Analysis Summary:")
    print(json.dumps(result, indent=2))

    if args.output:
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\n📁 Results saved to {args.output}")

if __name__ == "__main__":
    main()
