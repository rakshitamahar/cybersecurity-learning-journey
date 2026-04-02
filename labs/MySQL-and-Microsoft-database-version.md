# 🧪 SQL Injection – Database Version (MySQL & Microsoft)

## 📌 Lab: Extract Database Version

### 🎯 Objective

Identify database version (MySQL / MSSQL)

---

### 🔍 Vulnerability Type

SQL Injection (UNION-based)

---

### ⚙️ Steps Performed

1. Found number of columns
2. Injected version query

---

### 💉 Payload Used

```sql
' UNION SELECT @@version, NULL --
```

---

### 🧠 Explanation

* `@@version` returns DB version
* Works for MySQL & SQL Server

---

### ✅ Result

Extracted database version successfully.

---

### 🛡️ Prevention

* Prepared statements
* ORM usage
* Input sanitization

---

### 📚 Learning Outcome

* Learned DB fingerprinting
* Understood cross-DB payloads

### 📸 Proof of Concept
<img width="1920" height="1080" alt="Lab - 4 - 3" src="https://github.com/user-attachments/assets/0076ed7d-2a64-4f53-8d22-353845e96f7e" />
<img width="1920" height="1080" alt="Lab - 4 - 2" src="https://github.com/user-attachments/assets/ce1d8051-1c60-4dcb-b4f8-36f05d655939" />
<img width="1920" height="1080" alt="Lab - 4 - 1" src="https://github.com/user-attachments/assets/07694649-0d14-411c-b6bf-786e3b350cf2" />
