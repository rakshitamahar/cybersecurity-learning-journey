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

### 📸 Proof of Concept

(Add screenshot here)

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
