# 📁 CASE FILE #003: TOTAL RECALL

**Clearance:** L300 (Inspector)  
**Location:** Floor 20 (The Archives)

![The Database](../../assets/object_database_terminal.png)

## 🕵️‍♂️ Mission Briefing
**From:** Chief Tensor  
**To:** Agent Vertex (You)  
**Subject:** Recurring Amnesia Event

> "Agent, we have a problem. Every time we redeploy the Safehouse container, your agent forgets everything.
>
> Yesterday, it interrogated a suspect. Today, it doesn't even know the suspect's name.
> This is unacceptable. An investigator needs a memory.
>
> **Your Orders:**
> 1.  **Provision** a secure SQL Database in the cloud.
> 2.  **Wire** your agent's brain to this database.
> 3.  **Persist** every conversation log."

---

## 🎯 Objectives
1.  **Infrastructure:** Create a Cloud SQL (PostgreSQL) instance.
2.  **Dependencies:** Install `cloud-sql-python-connector` and `SQLAlchemy`.
3.  **Code:** Implement a `Memory` class that saves/loads chat history.

## 🛠️ The Toolkit
*   **Cloud SQL:** Managed PostgreSQL.
*   **SQLAlchemy:** The ORM (Object Relational Mapper).
*   **IAM Auth:** Secure connection (No hardcoded passwords!).

## ✈️ Pre-Flight Check
1.  **Activate Environment:** `source ../../.venv/bin/activate`
2.  **Enable APIs:** `gcloud services enable sqladmin.googleapis.com`

---

## 🚀 Start Your Investigation

### Step 1: The Missing Link
Open `missions/mission-03/start/agent.py`.
You will see the agent has no memory. It just loops.

### 🆘 Hints (Classified)

<details>
<summary>🔍 Hint 1: connecting to Cloud SQL</summary>

Use the connector to get a secure connection object:
```python
from google.cloud.sql.connector import Connector

connector = Connector()
def getconn():
    conn = connector.connect(
        "project:region:instance",
        "pg8000",
        user="service-account",
        db="enigma_db",
        enable_iam_auth=True
    )
    return conn
```
</details>

<details>
<summary>🔍 Hint 2: The Schema</summary>

You need a table.
```sql
CREATE TABLE chat_logs (
    id SERIAL PRIMARY KEY,
    role VARCHAR(50),
    content TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
</details>

---

## 🏆 Submission
Run the agent. Chat with it. Restart it.
If it remembers your name, you have succeeded.
Run the validator:
```bash
python ../../tools/validate_mission.py --mission 03 --instance YOUR_INSTANCE_NAME
```
