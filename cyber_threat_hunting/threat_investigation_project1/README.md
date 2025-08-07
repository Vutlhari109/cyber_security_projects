# 🕵️‍♂️ Cyber Investigation: Suspicious Domains & Threat Intelligence

This repository contains a documentation of my ethical cybercrime investigation into a network of suspicious domains, potentially connected through infrastructure or behavior patterns.

> ⚠️ **Disclaimer**: This investigation was conducted for educational, cybersecurity training, and threat intelligence learning purposes only. No active exploitation was performed. All observations were made through passive reconnaissance, open-source intelligence (OSINT), and public data. I fully understand and respect digital rights and privacy laws.  

---

## 🎯 Objective

To simulate a real-world cybercrime investigation by identifying, clustering, and analyzing suspicious domain behaviors, potentially linked malicious infrastructure, and sketchy operations.

---

## 📁 Contents

- `reports/` - Screenshots, investigation notes, and passive recon results
- `logs/` - WHOIS data, IP history, DNS info
- `threat_profiles/` - Domain relationships and clustering hypotheses
- `src/` - Scripts for passive lookups and analysis
- `screenshots/` - Captured browser behaviors (403s, redirects, errors)
- `README.md` - This file
- `LICENSE` - Legal disclaimer and license

---

## 🔍 Investigation Summary (Phase 1)

### 🧩 Identified Domains

> These domains appear to exhibit suspicious behavior such as:
> - Returning 403 Forbidden to normal visitors
> - Possible geo-IP filtering or bot detection
> - Passive DNS overlaps
> - Similar WHOIS patterns
> - Hidden content unless triggered by attacker-side mechanism

**Domains under investigation (Cluster 1):**

- `gradapplicationhelpfund.com`
- `myworld.com.np`
- `ambassadorshipregistration.org`
- `stepbystepfoundation.org`
- `2024universitygrants.com`
- (more redacted for safety)

### 🌐 Observations

- **403 Forbidden** on direct access (possible cloaking)
- Some domains are **inactive but registered**
- Others redirect only under certain conditions (via agent/IP/userpath)
- Some domains **used URLs similar to government programs or aid organizations** — this raises red flags
- **WHOIS** and **IP infrastructure** hints at clustering
- Hosting providers and registrars sometimes overlap
- Suspected **victim-specific payload delivery**

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| `whois` | Domain registration details |
| `nslookup` / `dig` | DNS & IP information |
| `Wireshark` | Packet inspection (passive only) |
| `SpiderFoot` | OSINT & Infrastructure mapping |
| `VirusTotal` | Reputation and history |
| `Shodan` | IP & port footprint |
| `Burp Suite (Passive)` | Behavior & redirect analysis |
| `ELK Stack (WIP)` | Log indexing & correlation |
| `Tor Browser` | Safe anonymous recon |
| `Screenshots` | Document behavior and anomalies |

---

## 💡 Challenges

- Many domains **hide content unless triggered** (phishing gates, cloaking)
- Limited access due to **403 responses**
- Couldn’t proceed further without **legal authorization** (warrant, permission, or working with a law enforcement agency)
- Concerns about **privacy laws**, risk of being flagged as invasive without proper channels
- Ethical line: Passive recon only, **no active scanning or intrusion**

---

## 🧠 What I Learned

- Real-world attackers often create **clusters of domains** tied to fake aid, jobs, or student programs
- Threat infrastructure can be **geo-targeted and cloaked**
- **Passive OSINT** can reveal a lot — but **legal boundaries** are real and must be respected
- Ethical hacking must always prioritize **user safety, privacy, and legality**
- Documenting and reporting suspicious behavior can help **build cybercrime intelligence portfolios**

---

## 🚫 Why I Stopped

I am close to detecting patterns that may expose criminal behavior. However, continuing the investigation without legal support or a digital forensic warrant could:

- Trigger attacker defenses
- Violate international cyber laws
- Expose me to liability

As a responsible ethical hacker and threat hunter, I am halting this phase and documenting what I found to date.

---

## 📬 What’s Next?

- Report suspicious domains to a **Computer Security Incident Response Team (CSIRT)** or CERT
- Continue my training in:
  - Network forensics
  - Malware analysis
  - Cybercrime investigation techniques
- Connect with security communities like:
  - **DFIR community**
  - **RedTeam Village**
  - **SANS Forums**
  - **Mitre ATT&CK and MISP**

---

## 👨‍💻 Author

**Vutlhari Mathebula**  
Cybercrime Threat Investigator (Trainee)  
- Focus: Network forensics, threat hunting, and OSINT  
- Tools: Wireshark, SpiderFoot, tcpdump, ELK, Metasploit, Burp Suite  
- Linkedin: [linkedin.com/in/vutlhari-mathebula-6b4660313/]  
- Email: [vutlharimathebula74@gmail.com]

---

## 🛡️ License & Ethics

This project is licensed under the [MIT License](LICENSE).  
All research was conducted ethically, with intent for learning and community safety.

If you're a security researcher or law enforcement official and need collaboration, feel free to reach out.

---

## 📸 Screenshots (Sample)

![] Screenshot Folder
---

## 🧠 Final Note

> _"In cyber forensics, knowing when to stop is just as important as knowing where to look."_  
> — Vutlhari Mathebula
---

