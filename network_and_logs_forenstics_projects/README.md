# 🕵️‍♂️ Digital Forensics & Incident Response (DFIR) Project

## 📌 Overview
This project demonstrates practical **network forensics** and **log analysis** skills using a simulated cyber incident.  
It combines **Wireshark packet captures**, **web server logs**, and **firewall events** to identify suspicious activity, reconstruct timelines, and provide actionable conclusions.

The goal: **Prove my ability to investigate, correlate, and report incidents** in a professional, evidence-driven manner.

---

## 📂 Project Structure
/pcap/ # Wireshark capture files (.pcap)
/logs/web/ # Web server access/error logs
/logs/firewall/ # Firewall connection and alert logs
/timelines/ # Chronological event reconstructions
/reports/ # Final forensics reports (PDF/Markdown)
README.md # Project description (this file)


---

## 🔍 Investigation Workflow
1. **Evidence Collection**  
   - Preserve original PCAPs, server logs, and firewall data.  
   - Normalize all timestamps to UTC.  

2. **Initial Triage**  
   - Identify suspicious domains, IPs, and unusual traffic patterns.  
   - Use `Wireshark` filters:  
     - `ip.addr == <target_ip>`  
     - `tls.handshake.type == 1` (Client Hello)  
     - `tls.record.length > 1000` (large TLS packets)  

3. **Correlation Across Sources**  
   - Link packet captures to web log entries (same IP/session ID).  
   - Cross-check with firewall alerts (connection attempts, blocks).  

4. **Timeline Reconstruction**  
   - Order events chronologically to show exact attack flow.  
   - Example:  
     ```
     2025-08-10T13:45:22Z | 192.168.1.88 | Web | GET /admin/login.php → 401 Unauthorized
     2025-08-10T13:45:24Z | 192.168.1.88 | Web | Successful login
     2025-08-10T13:45:25Z | 192.168.1.88 | Web | GET /settings.php (sensitive page)
     2025-08-10T13:45:26Z | 192.168.1.88 | Net | TLS handshake with 203.0.113.77 (public IP)
     ```

5. **Analysis & Findings**  
   - Suspicious domain resolution from Google DNS.  
   - Brute force login followed by access to sensitive routes.  
   - Possible exfiltration over encrypted TLS channel.

6. **Recommendations**  
   - Block malicious IPs/domains at perimeter firewall.  
   - Implement WAF rules for `/admin` and `/settings.php`.  
   - Enforce account lockout after failed login attempts.  

---

## 🛠 Tools Used
- **Wireshark** – packet capture & protocol analysis  
- **ELK Stack** – log aggregation & search  
- **Linux CLI** – grep, awk, netstat, whois for investigation  
- **Timeline Tools** – Timesketch, Excel, custom Python scripts  

---

## 📊 Example Evidence
**Suspicious TLS Certificate:**


---

## 🔍 Investigation Workflow
1. **Evidence Collection**  
   - Preserve original PCAPs, server logs, and firewall data.  
   - Normalize all timestamps to UTC.  

2. **Initial Triage**  
   - Identify suspicious domains, IPs, and unusual traffic patterns.  
   - Use `Wireshark` filters:  
     - `ip.addr == <target_ip>`  
     - `tls.handshake.type == 1` (Client Hello)  
     - `tls.record.length > 1000` (large TLS packets)  

3. **Correlation Across Sources**  
   - Link packet captures to web log entries (same IP/session ID).  
   - Cross-check with firewall alerts (connection attempts, blocks).  

4. **Timeline Reconstruction**  
   - Order events chronologically to show exact attack flow.  
   - Example:  
     ```
     2025-08-10T13:45:22Z | 192.168.1.88 | Web | GET /admin/login.php → 401 Unauthorized
     2025-08-10T13:45:24Z | 192.168.1.88 | Web | Successful login
     2025-08-10T13:45:25Z | 192.168.1.88 | Web | GET /settings.php (sensitive page)
     2025-08-10T13:45:26Z | 192.168.1.88 | Net | TLS handshake with 203.0.113.77 (public IP)
     ```

5. **Analysis & Findings**  
   - Suspicious domain resolution from Google DNS.  
   - Brute force login followed by access to sensitive routes.  
   - Possible exfiltration over encrypted TLS channel.

6. **Recommendations**  
   - Block malicious IPs/domains at perimeter firewall.  
   - Implement WAF rules for `/admin` and `/settings.php`.  
   - Enforce account lockout after failed login attempts.  

---

## 🛠 Tools Used
- **Wireshark** – packet capture & protocol analysis  
- **ELK Stack** – log aggregation & search  
- **Linux CLI** – grep, awk, netstat, whois for investigation  
- **Timeline Tools** – Timesketch, Excel, custom Python scripts  

---

## 📊 Example Evidence
**Suspicious TLS Certificate:**

Issuer: C=US, O=Let's Encrypt, CN=R3
Subject: CN=admin.portal-secure.net
Valid From: Aug 1 00:00:00 2025 GMT
Valid To: Oct 30 23:59:59 2025 GMT
Key: RSA 2048-bit

markdown
Copy code

**Firewall Alert:**
[2025-08-10 13:45:20] ALERT: Brute force login detected
SRC=192.168.1.88 DST=203.0.113.77 PORT=443 PROTO=TCP
ACTION=ALLOW (post-auth)

yaml
Copy code

---

## 📄 Deliverables
- ✅ **Forensics Report** – professional, evidence-based write-up  
- ✅ **Full Timeline** – minute-by-minute reconstruction  
- ✅ **Indicators of Compromise (IOCs)** – domains, IPs, hashes, certs  
- ✅ **Mitigation Recommendations** – actionable security steps  

---

## 📬 Contact
If you’re looking for someone who can **turn raw network and log data into actionable security intelligence**, reach out:

**Name:**  Vutlhari Mathebula 
**Email:** vutlharimathebula74@gmail.com  
**LinkedIn:** linkedin.com/in/vutlhari-mathebula-6b4660313  
**GitHub:** github.com/Vutlhari109 
