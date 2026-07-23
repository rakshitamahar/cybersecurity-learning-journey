# Automated Network Reconnaissance & Enumeration Toolkit

## Overview
A modular reconnaissance tool designed to streamline the initial phases of a security assessment. This script chains industry-standard utilities (`theHarvester`, `Nmap`, and `Gobuster`) to map attack surfaces and output structured enumeration reports.

## Features
- **Attack Surface Discovery:** Executes passive reconnaissance via theHarvester to collect subdomains and exposed endpoints.
- **Port Scanning & Fingerprinting:** Automates Nmap execution to identify open ports and service versions.
- **Web Directory Enumeration:** Automatically routes discovered web servers into Gobuster to uncover hidden directories and files.
- **Automated Logging:** Consolidates all raw tool outputs into structured timestamped text files for reporting.

## Tools & Concepts
- **Languages/Shell:** Python / Bash
- **Core Utilities:** Nmap, Gobuster, theHarvester
- **Security Concepts:** Active/Passive Recon, Port Scanning, Service Enumeration, Directory Brute-Forcing
