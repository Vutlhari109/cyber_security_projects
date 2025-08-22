"""
Volatility 3 Forensics Investigation Template
Author: Vutlhari Mathebula
Purpose: Investigate memory dumps for malware, intrusions, and forensic artifacts.
Instructions:
- Place this script in your volatility3 folder.
- Replace MEMORY_DUMP_PATH with your RAM image path.
- Run modules one by one to analyze the memory.
"""

MEMORY_DUMP_PATH = r"C:\Users\vutlh\Documents\charlie-2009-12-08.mddramimage"
PROFILE = "windows"  # Volatility3 auto-detects, mostly leave as windows

# -----------------------------
# Import Volatility 3 modules
# -----------------------------
from volatility3.framework import contexts, interfaces, exceptions
from volatility3.cli import text_renderer
from volatility3.cli import framework

# Example function to run a plugin
def run_plugin(plugin_name, **kwargs):
    """
    Executes a Volatility3 plugin and prints results.
    plugin_name: str, e.g. "windows.pslist.PsList"
    kwargs: plugin-specific arguments
    """
    print(f"\n=== Running {plugin_name} ===\n")
    try:
        cmd = f"python vol.py -f \"{MEMORY_DUMP_PATH}\" {plugin_name}"
        for k, v in kwargs.items():
            cmd += f" --{k} {v}"
        print(f"Run this in CMD/Powershell:\n{cmd}\n")
    except Exception as e:
        print(f"Error running plugin {plugin_name}: {e}")

# ---------------------------------------
# Module explanations and forensic steps
# ---------------------------------------

# 1. windows.pslist / windows.pstree / windows.psscan
# -> Lists running processes, their parent-child relationships, and hidden processes
# -> Use pstree to see process hierarchy
# -> Use psscan to detect terminated or hidden processes in memory
# AFTER: Note suspicious processes, unusual parent-child chains, unknown binaries.
run_plugin("windows.pslist.PsList")
run_plugin("windows.pstree.PsTree")
run_plugin("windows.psscan.PsScan")

# 2. windows.cmdline.CmdLine
# -> Extracts command line arguments of processes
# -> Check for network paths, mapped drives, remote execution, suspicious flags
# AFTER: Look for commands like memory dump tools, reverse shells, or malware execution.
run_plugin("windows.cmdline.CmdLine")

# 3. windows.handles.Handles
# -> Shows objects a process has opened: files, mutexes, ports, registry keys
# -> Look for suspicious files or network handles (e.g., \\192.168.1.1\m57\ram)
# AFTER: Identify evidence of remote connections, persistence, or inter-process activity.
run_plugin("windows.handles.Handles", pid=1384)

# 4. windows.dlllist.DllList
# -> Lists all DLLs loaded by each process
# -> Check for injected or unsigned DLLs, unexpected modules
# AFTER: Dump suspicious DLLs for analysis and malware confirmation.
run_plugin("windows.dlllist.DllList")

# 5. windows.malware.malfind.Malfind
# -> Scans memory for injected or suspicious code regions
# -> Highlights hidden malicious threads or code in legitimate processes
# AFTER: Dump detected regions for offline malware analysis.
run_plugin("windows.malware.malfind.Malfind")

# 6. windows.dumpfiles.DumpFiles
# -> Extracts embedded files from memory (executables, documents, scripts)
# -> Can capture attacker RAM dumps or dropped malware
# AFTER: Save files, scan with antivirus or analyze manually with YARA/strings.
run_plugin("windows.dumpfiles.DumpFiles")

# 7. windows.amcache.Amcache
# -> Provides history of executed binaries from Windows artifact
# -> Verify suspicious execution timestamps and binaries
# AFTER: Correlate with pslist and shimcache for timeline reconstruction.
run_plugin("windows.amcache.Amcache")

# 8. windows.shimcachemem.ShimcacheMem
# -> Checks Application Compatibility Cache for programs run on system
# -> Detect anomalies or programs not listed in Amcache
# AFTER: Detect hidden executions and persistence mechanisms.
run_plugin("windows.shimcachemem.ShimcacheMem")

# 9. windows.sessions.Sessions
# -> Lists user sessions, logons, active users
# -> Identify unauthorized or suspicious logins
# AFTER: Map processes to users to find attacker accounts or compromised sessions.
run_plugin("windows.sessions.Sessions")

# 10. windows.registry.* (UserAssist, ScheduledTasks, Certificates)
# -> Investigates registry artifacts for persistence and configuration
# -> Detect auto-start malware, rogue scheduled tasks, suspicious certificates
# AFTER: Dump registry keys, confirm malware persistence.
run_plugin("windows.registry.userassist.UserAssist")
run_plugin("windows.registry.scheduled_tasks.ScheduledTasks")

# 11. windows.memmap.Memmap / windows.vadwalk.VadWalk / windows.vadinfo.VadInfo
# -> Map virtual memory areas, analyze allocations
# -> Detect injected code, suspicious VAD regions
# AFTER: Identify memory-resident malware or hidden injected regions.
run_plugin("windows.memmap.Memmap")
run_plugin("windows.vadwalk.VadWalk")

# 12. windows.strings.Strings / regexscan.RegExScan
# -> Extract readable strings from memory
# -> Use regex to search for passwords, keys, IPs, URLs, suspicious commands
# AFTER: Collect credentials or network indicators for forensic correlation.
run_plugin("windows.strings.Strings")
run_plugin("regexscan.RegExScan", regex="password|key|token")

# 13. windows.timers.Timers / windows.callbacks.Callbacks
# -> Lists kernel timers and callbacks
# -> Can reveal rootkits, scheduled malicious activity
# AFTER: Investigate unusual kernel timers or callbacks tied to suspicious processes.
run_plugin("windows.callbacks.Callbacks")
run_plugin("windows.timers.Timers")

# 14. windows.ldrmodules.LdrModules / windows.driverirp.DriverIrp / windows.drivermodule.DriverModule
# -> Check loaded drivers and kernel modules
# -> Detect unsigned or malicious drivers
# AFTER: Dump suspicious drivers for offline analysis and persistence check.
run_plugin("windows.ldrmodules.LdrModules")
run_plugin("windows.drivermodule.DriverModule")

# 15. windows.privileges.Privs
# -> Check process privilege levels
# -> Detect SYSTEM or elevated processes that shouldn’t have high privileges
# AFTER: Highlight processes the attacker used to escalate access.
run_plugin("windows.privileges.Privs")

# 16. windows.mbrscan.MBRScan
# -> Scan Master Boot Record
# -> Detect bootkits or disk-level malware
# AFTER: Backup and analyze suspicious MBR regions.
run_plugin("windows.mbrscan.MBRScan")

# 17. windows.vadregexscan.VadRegExScan
# -> Scan memory-mapped files for custom regex patterns
# -> Can locate malware, keys, IP addresses, or credentials
# AFTER: Dump matches for investigation and correlate with strings/regexscan results.
run_plugin("windows.vadregexscan.VadRegExScan", regex=".*")

# ----------------------
# Final steps after running all modules
# ----------------------
# 1. Correlate pslist, pstree, psscan, amcache, and shimcache results.
# 2. Dump suspicious processes/files for offline analysis.
# 3. Map network handles and open ports (if network artifacts are found).
# 4. Document findings for forensic report.
# 5. If malware detected, hash binaries and upload to VirusTotal / sandbox.
