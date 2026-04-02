# Portswigger SQL Injection Labs

Lab 1: SQL Injection Login Bypass
Objective: Bypass the login functionality using SQL injection.

Vulnerability Type:SQL Injection (Authentication Bypass)

Steps Performed:
1. Opened the login page
2. Intercepted request (or tested input manually)
3. Injected payload in username field

Payload Used: ' OR 1=1 --
Explanation:
OR 1=1 is always TRUE
This bypasses authentication
The application logs in without valid credentials
<img width="1920" height="1080" alt="SQL lab2" src="https://github.com/user-attachments/assets/d796230a-8b3f-457c-8ca8-a6e8ab980f55" />
<img width="1920" height="1080" alt="LAb-2" src="https://github.com/user-attachments/assets/f506de1a-731f-43d4-b3bf-77f053f84563" />

Result: Successfully bypassed login without knowing credentials.

Prevention:
Use parameterized queries
Input validation
Avoid dynamic SQL queries

Learning Outcome:
Understood authentication bypass
Learned basic SQL injection logic
