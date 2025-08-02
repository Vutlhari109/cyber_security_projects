# 🕵️ Wireshark Network Packet Analysis

## 🎯 Objective

Capture and analyze HTTP traffic to identify hidden endpoints, login attempts, and API behavior of a locally hosted vulnerable web application using Wireshark.

---

## 🧰 Tools Used

* **Wireshark** – Passive network packet sniffer
* **Kali Linux** – Host system for analysis
* **Local Vulnerable Web App** – Juice Shop or similar

---

## 📁 Files Included

* `wireshark_network_capture.pcapng` – Raw packet capture file with full network trace

> ⚠️ This file is binary and can only be opened in Wireshark

---

## 🔍 Key Observations

### ✅ Hidden API Routes

* Discovered undocumented route:

  ```
  ```

GET /rest/admin HTTP/1.1

```
- Found by analyzing plain HTTP traffic, without interacting or logging in

### 🔐 Login Attempt Trace
- Captured a POST login request:
```

POST /rest/user/login HTTP/1.1
Host: 10.66.170.47:3000
Content-Type: application/json

````
- Contains sensitive fields like email and password (in plaintext if HTTPS not used)

### 🧠 Localhost IP Context
- IP address used for analysis: `10.66.170.47`
- Hosted on local network and analyzed in real-time

---

## 🧪 Filters Used
```bash
http
ip.addr == 10.66.170.47
http.request.method == "POST"
````

These filters helped isolate meaningful traffic from noisy packet streams.

---

## 🧠 Insights

> "Wireshark is like a police dog: it sniffs hidden items (like /rest/admin), but doesn’t touch or interact—just reveals."

* Unlike Burp Suite (active web proxy), Wireshark is passive—it logs but doesn't interact.
* Helpful in forensic analysis and evidence collection without alerting the system.

---

## 📚 What I Learned

* Passive network sniffing and packet inspection
* Isolating login attempts and hidden endpoints from packet captures
* Understanding TCP streams and HTTP methods

---

## 📌 Portfolio Use

This `.pcapng` capture demonstrates my ability to:

* Monitor and analyze traffic
* Extract evidence and behavior from a network stream
* Perform digital forensics in a local ethical hacking lab

> Great for roles in Cybercrime Investigation, Threat Hunting, or Digital Forensics.

---

## 👨‍💻 Author

**Vutlhari Mathebula**
Aspiring Cybercrime & Digital Forensics Analyst
