---
id: enigma-mission-02-safehouse
description: Mission 02: Containerize and deploy your AI Agent to Cloud Run.
status: published
keywords: docType:Codelab, skill:Intermediate, product:CloudRun, product:GoogleCloud, language:Python
categories: cloud-run, docker, python
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

# Mission 02: The Safehouse
## Overview
Duration: 1:00

### The Briefing

**Subject:** Containment Protocol

> "The suspect (your Agent) is currently running loose on your local machine. This is unacceptable.
> We need to move it to **The Safehouse**—a secure, auto-scaling container environment in the Cloud."

![The Safehouse](img/location_server_room.png)

### What You'll Learn
*   How to write a **Dockerfile** for a Python AI Agent.
*   How to build container images using **Cloud Build**.
*   How to deploy to **Google Cloud Run**.

### What You Need
*   Completion of [Mission 01](../google-cloud-enigma-mission-01-informant/index.lab.md).
*   A Google Cloud Project with **Billing Enabled**.

## Container Theory
Duration: 5:00

### Why Cloud Run?
Your local laptop (Floor 1) cannot handle the global traffic we expect.
Cloud Run allows us to:
1.  **Scale to Zero:** If no one is interrogating, it costs $0.
2.  **Scale to Infinity:** If The Null Pointer attacks, it scales up.
3.  **Secure:** Isolated environment.

### The Strategy
1.  **Define:** Create a receipt (`Dockerfile`) for the environment.
2.  **Build:** Cook the meal (`Container Image`).
3.  **Serve:** Open the restaurant (`Cloud Run Service`).

## Step 1: The Dockerfile
Duration: 10:00

Navigate to `missions/mission-02/start/`.
Create a file named `Dockerfile` (no extension).

### The Blueprint
Copy the following into your `Dockerfile`:

```dockerfile
# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the code
COPY . .

# 6. Run the agent when the container launches
# Note: For Cloud Run, we usually need a web server (Flask/FastAPI).
# But for this level, we are deploying a Worker (Console App).
CMD ["python", "agent.py"]
```

> aside negative
**Critical Info:** Cloud Run Services typically require listening on `PORT 8080`.
Since our `agent.py` is a CLI loop, it will crash in a standard Cloud Run Service because it doesn't open a web port.
**For this Mission, we will deploy it as a Cloud Run JOB.**

## Step 2: Build the Image
Duration: 10:00

We will use Google Cloud Build to build the image without Docker installed locally.

1.  **Enable APIs:**
    ```bash
    gcloud services enable cloudbuild.googleapis.com run.googleapis.com
    ```

2.  **Submit the Build:**
    ```bash
    gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/enigma-agent:v1 .
    ```

Wait for the success message `SUCCESS`.

## Step 3: Deploy the Job
Duration: 5:00

Since our agent is a script (not a web server), we deploy it as a **Job**.

```bash
gcloud run jobs create enigma-agent-job \
  --image gcr.io/${GOOGLE_CLOUD_PROJECT}/enigma-agent:v1 \
  --region us-central1
```

### Execute
Now, run the job to see if it works.

```bash
gcloud run jobs execute enigma-agent-job
```

Go to the [Cloud Console](https://console.cloud.google.com/run/jobs) to view the logs. You should see "Agent Vertex is online."

## Mission Debrief
Duration: 1:00

**Congratulations.**
The suspect is now contained in a repeatable, scalable environment.

### Next Assignment
The agent is secure, but it has no memory. Every time the container restarts, it forgets everything.
We need to give it a database.

**Next Mission:** [The Archive (Cloud SQL)](../google-cloud-enigma-mission-03-recall/index.lab.md)

