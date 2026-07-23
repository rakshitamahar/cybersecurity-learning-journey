# 🧪 SQL Injection – WHERE Clause (Hidden Data Retrieval)

## 📌 Lab: Retrieve Hidden Data

### 🎯 Objective

Access restricted/hidden data using SQL injection

---

### 🔍 Vulnerability Type

SQL Injection (WHERE clause)

---

### ⚙️ Steps Performed

1. Identified filter condition
2. Modified query logic

---

### 💉 Payload Used

```sql
' OR 1=1 --
```

---

### 🧠 Explanation

* `OR 1=1` makes condition TRUE
* Bypasses filtering restrictions
* Displays hidden data

---

### 📸 Proof of Concept

<img width="1920" height="1036" alt="Screenshot 2026-03-19 225257" src="https://github.com/user-attachments/assets/24f6fa6a-6eed-465e-84fc-a8fd5c7292af" />
<img width="1920" height="1080" alt="Lab-1" src="https://github.com/user-attachments/assets/50ff5c8f-9d16-4db3-9fac-c229e0e3bde7" />

---

### ✅ Result

Retrieved hidden products/data.

---

### 🛡️ Prevention

* Parameterized queries
* Strict filtering
* Use ORM

---

### 📚 Learning Outcome

* Learned logic manipulation
* Understood WHERE clause exploitation
