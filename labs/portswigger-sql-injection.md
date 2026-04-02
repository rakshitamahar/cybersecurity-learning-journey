# Portswigger SQL Injection Labs
## 📌 Lab 1: SQL Injection Login Bypass

### 🎯 Objective
Bypass the login functionality using SQL injection.

### 🔍 Vulnerability Type
SQL Injection (Authentication Bypass)

Steps Performed:
1. Opened the login page
2. Intercepted request (or tested input manually)
3. Injected payload in username field

### 💉 Payload Used
```sql
' OR 1=1 --

```markdown
### 🧠 Explanation
- `OR 1=1` is always TRUE  
- This condition bypasses authentication checks  
- The application grants access without validating credentials

### 📸 Proof of Concept
<img width="1920" height="1080" alt="SQL lab2" src="https://github.com/user-attachments/assets/d796230a-8b3f-457c-8ca8-a6e8ab980f55" />
<img width="1920" height="1080" alt="LAb-2" src="https://github.com/user-attachments/assets/f506de1a-731f-43d4-b3bf-77f053f84563" />

Result: Successfully bypassed login without knowing credentials.

### 🛡️ Prevention
- Use parameterized queries (prepared statements)  
- Validate and sanitize user inputs  
- Avoid dynamic SQL queries

### 📚 Learning Outcome
- Learned how SQL injection bypasses authentication  
- Understood how TRUE conditions affect queries  
- Gained hands-on experience with real lab exploitation
