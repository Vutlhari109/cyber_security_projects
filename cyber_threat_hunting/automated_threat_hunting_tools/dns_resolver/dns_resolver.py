import dns.resolver

def resolve_dns(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    results = {}

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            results[rtype] = [str(rdata) for rdata in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            results[rtype] = []

    return results

if __name__ == "__main__":
    domain = input("Enter domain to resolve DNS: ").strip()
    dns_data = resolve_dns(domain)

    for rtype, records in dns_data.items():
        print(f"\n[{rtype} Records]")
        if records:
            for record in records:
                print(f" - {record}")
        else:
            print(" - None found")
