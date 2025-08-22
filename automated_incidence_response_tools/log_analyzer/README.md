# 📄 Log File Analyzer — Suspicious Access & Brute Force Detection

Scans Apache or Nginx logs for:
- Brute-force attempts (401/403 errors)
- Suspicious path access (e.g. `/admin`, `/login`, `/wp-login.php`)
- Top active IPs
- Unusual request frequency

## 🔧 Usage

```bash
python analyze_logs.py sample_logs/access.log --output report.json
