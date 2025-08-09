# Scenario 5: SSH Brute Force Login Attempts

## Description
This capture shows multiple SSH connection attempts from client `192.168.1.100` to server `203.0.113.5` on port 22.

## Key Observations
- Multiple TCP sessions start and end quickly.
- The client attempts to log in with different usernames (`admin`, `root`).
- No evidence of successful login; sessions close soon after attempts.
- This pattern is typical of brute force or credential guessing attacks.

## Conclusion
Repeated login attempts with different usernames indicate a brute force attack. Monitoring and blocking such behavior is important to prevent unauthorized access.
