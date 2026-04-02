# 🧪 SQL Injection – Querying Database Type & Version (Oracle)
## 📌 Lab 2 : Oracle Database Version Extraction

### 🎯 Objective: Determine the database type and version.

### 🔍 Vulnerability Type: SQL Injection (UNION-based)

### ⚙️ Steps Performed:
1. Identified injectable parameter
2. Determined number of columns using:

   ```sql
   ' UNION SELECT NULL FROM dual --
   ```
3. Extracted version using Oracle-specific table

---

### 💉 Payload Used

```sql
' UNION SELECT banner, NULL FROM v$version --
```

---

### 🧠 Explanation

* `v$version` is an Oracle system table
* `banner` contains version information
* `dual` is a dummy table used in Oracle

---

### ✅ Result

Successfully retrieved Oracle database version.

---

### 🛡️ Prevention

* Parameterized queries
* Input validation
* Least privilege access

---

### 📚 Learning Outcome

* Learned Oracle-specific SQL injection techniques
* Understood use of system tables

### 📸 Proof of Concept
<img width="1920" height="1080" alt="Lab 3 - 5" src="https://github.com/user-attachments/assets/107738f7-b205-418f-8b19-44e33bef0d01" />
<img width="1920" height="1080" alt="LAb 3 - 4" src="https://github.com/user-attachments/assets/84e947b9-20d2-465e-968a-d8c487650c97" />
<img width="1920" height="1080" alt="lab 3 - 3" src="https://github.com/user-attachments/assets/f7ebda9a-2e42-4c0e-a9a3-2103475e3175" />
<img width="1920" height="1080" alt="Lab 3 - 2" src="https://github.com/user-attachments/assets/2dbdf33e-2ec6-4138-a4ea-a4d5a3c261ae" />
<img width="1920" height="1080" alt="Lab 3 - 1" src="https://github.com/user-attachments/assets/51894f8e-a6d2-4272-93c8-122f3d2ae75e" />
