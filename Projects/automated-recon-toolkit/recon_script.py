#!/usr/bin/env python3
import subprocess
import sys
import os

def run_command(command, description):
    """Helper function to run shell commands safely and print status."""
    print(f"\n[+] Starting: {description}")
    print(f"Executing: {' '.join(command)}")
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(f"[✔] Successfully completed: {description}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[✘] Error executing {description}: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 recon_script.py <target_domain_or_ip>")
        sys.exit(1)

    target = sys.argv[1]
    output_dir = f"recon_results_{target.replace('.', '_')}"
    
    # Create an output directory for logs
    os.makedirs(output_dir, exist_ok=True)
    print(f"[+] Results will be saved in directory: {output_dir}/")

    # 1. Passive Recon with theHarvester
    harvester_output = os.path.join(output_dir, "harvester_out.txt")
    harvester_cmd = ["theHarvester", "-d", target, "-b", "all", "-f", harvester_output]
    run_command(harvester_cmd, "Passive Reconnaissance via theHarvester")

    # 2. Port Scanning & Version Fingerprinting with Nmap
    nmap_output = os.path.join(output_dir, "nmap_out.txt")
    nmap_cmd = ["nmap", "-sV", "-T4", "-p-", target, "-oN", nmap_output]
    run_command(nmap_cmd, "Port Scanning & Service Enumeration via Nmap")

    # 3. Web Directory Enumeration with Gobuster (Assuming standard HTTP port 80)
    # Note: In a more advanced script, you can parse Nmap output to dynamically find open HTTP ports.
    gobuster_output = os.path.join(output_dir, "gobuster_out.txt")
    target_url = f"http://{target}"
    wordlist_path = "/usr/share/wordlists/dirb/common.txt" # Update path based on your system dictionary
    
    if os.path.exists(wordlist_path):
        gobuster_cmd = ["gobuster", "dir", "-u", target_url, "-w", wordlist_path, "-o", gobuster_output]
        run_command(gobuster_cmd, "Directory Brute-Forcing via Gobuster")
    else:
        print(f"[!] Wordlist not found at {wordlist_path}. Skipping Gobuster.")

    print(f"\n[✔] Reconnaissance workflow finished for target: {target}")

if __name__ == "__main__":
    main()
