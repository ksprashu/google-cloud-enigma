---
id: enigma-mission-03-recall
description: Mission 03: Connect your Agent to Cloud SQL for long-term memory.
status: published
keywords: docType:Codelab, skill:Intermediate, product:CloudSQL, product:GoogleCloud, language:Python
categories: cloud-sql, python, database
feedback link: https://github.com/ksprashu/google-cloud-enigma/issues
authors: Prashanth Subrahmanyam
layout: paginated
project: /devsite/_project.yaml
book: /devsite/_book.yaml

---
{# disableFinding(METADATA_BOOK) #}
{# disableFinding(METADATA_PROJECT) #}
{# disableFinding(HEADING_NO_ID_H2) #}
{# disableFinding(HEADING_NO_ID_H3) #}

# Mission 03: Total Recall

## Overview
Duration: 1:00

### The Briefing

**Subject:** Cognitive Failure (Amnesia)

> "We have a crisis. Our Agent is brilliant but has the memory of a goldfish.
> Every time the server restarts, the case files vanish.
> We need to connect it to the **Central Police Database**."

![The Database](img/object_database_terminal.png)

### What You'll Learn
*   How to provision a **Cloud SQL (PostgreSQL)** instance.
*   How to use the **Cloud SQL Python Connector** (No explicit passwords!).
*   How to implement **Long-Term Memory** in an AI Agent.

### What You Need
*   Completion of [Mission 02](../google-cloud-enigma-mission-02-safehouse/index.lab.md).
*   A Google Cloud Project.

## Infrastructure Setup
Duration: 10:00

### 1. Enable APIs
We need the SQL Admin API to manage the database.

```bash
gcloud services enable sqladmin.googleapis.com
```

### 2. Create the Database
This will take a few minutes. Grab a coffee.

```bash
gcloud sql instances create enigma-db \
    --database-version=POSTGRES_15 \
    --cpu=1 \
    --memory=3840MB \
    --region=us-central1 \
    --root-password=supersecret
```

### 3. Create a User & Database
```bash
gcloud sql databases create agent_memory --instance=enigma-db
gcloud sql users create vertex_agent --instance=enigma-db --password=let_me_in
```

## The Code: Connecting
Duration: 15:00

### 1. Install Dependencies
Navigate to `missions/mission-03/start/` and install the requirements.
We need `cloud-sql-python-connector` and `pg8000`.

### 2. The Connector
In `memory.py`, we will write a function to connect securely.

```python
from google.cloud.sql.connector import Connector
import sqlalchemy

def init_connection_pool(instance_connection_name, db_user, db_pass, db_name):
    connector = Connector()

    def getconn():
        conn = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name
        )
        return conn

    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )
    return pool
```

## The Code: Remembering
Duration: 10:00

### 1. The Table
We need to create a table to store the chat.

```python
def create_table(pool):
    with pool.connect() as db_conn:
        db_conn.execute(sqlalchemy.text(
            "CREATE TABLE IF NOT EXISTS memory "
            "(id SERIAL PRIMARY KEY, role VARCHAR(50), content TEXT)"
        ))
        db_conn.commit()
```

### 2. Saving & Loading
Modify your agent to:
1.  **Load** previous rows from `memory` table on startup.
2.  **Insert** new rows into `memory` table after each message.

## Verification
Duration: 5:00

Run your agent locally.
1.  Tell it: "My name is Detective Smith."
2.  Exit the script.
3.  Run it again.
4.  Ask: "What is my name?"

If it answers "Detective Smith", you have cured the amnesia.

## Mission Debrief
Duration: 1:00

**Congratulations.**
Your Agent now possesses Long-Term Memory. It is becoming a true partner.

### Next Assignment
The Agent remembers *facts*, but it cannot read *documents*.
The Null Pointer left a manifesto PDF. We need to ingest it.

**Next Mission:** The Archive (Vector Search & RAG).
