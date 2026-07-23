# Web Application Security & SQL Injection Portfolio

## Overview
A documented portfolio of hands-on web vulnerability assessment labs completed via the PortSwigger Web Security Academy. This project demonstrates practical offensive security techniques, traffic analysis using Burp Suite, and defensive mitigation strategies aligned with the OWASP Top 10.

## Key Techniques Covered
- **Retrieving Hidden Data:** Modifying WHERE clauses using comment indicators (`--`) and boolean logic (`OR 1=1`) to bypass display filters.
- **Authentication Bypass:** Subverting application logic to log into user accounts without valid credentials.
- **Union-Based Data Extraction:** Leveraging the `UNION` operator to retrieve data from external database tables.

## Tools & Environment
- **Proxy/Testing:** Burp Suite (Repeater, Proxy, Intercept)
- **Target Platform:** PortSwigger Web Security Labs
- **Core Concepts:** HTTP Request/Response analysis, SQL syntax, Parameter Manipulation

## Remediation & Secure Coding
Implemented and reviewed parameterized queries (Prepared Statements) to ensure untrusted user input is treated strictly as data rather than executable query code.
