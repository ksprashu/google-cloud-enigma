# 🕵️‍♂️ Project Enigma: The Cloud Bureau

![Project Enigma](assets/logo_banner_main.png)

> **Clearance Level:** RESTRICTED  
> **Status:** ACTIVE  
> **Bureau Chief:** Tensor

Welcome to the **Cloud Bureau of Investigation (CBI)**.
You have been recruited as an **AI Detective**. Your mission is to hunt down **The Null Pointer**, a rogue entity that is destabilizing the global compute grid.

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/ksprashu/google-cloud-enigma&cloudshell_tutorial=codelabs/google-cloud-enigma-mission-01-informant/index.lab.md)

---

## 🧩 The Objective
You will build, deploy, and scale your own **AI Agent** using Google Cloud's most advanced technology.

*   **Floors 1-10:** Build the Brain (Gemini, Python).
*   **Floors 11-20:** Build the Body (Cloud Run, SQL).
*   **Floors 21-30:** Build the Memory (Vector Search, RAG).
*   **Floors 31-50:** Build the Agency (Multi-Agent Systems).

## 🚀 Getting Started

### 1. Acquire Credentials
You need a **Gemini API Key** to operate your detective tools.
*   [Get your Key here](https://aistudio.google.com/app/apikey)
*   *Security Warning:* Never commit this key to Git.

### 2. Initialize Environment
If you clicked the **Open in Cloud Shell** button above, your terminal is ready.
Otherwise, clone this repo and set up your workstation:

```bash
# 1. Create a virtual environment
python3 -m venv .venv

# 2. Activate it (Mac/Linux)
source .venv/bin/activate
# (Windows: .venv\Scripts\activate)

# 3. Set your credentials
export GEMINI_API_KEY="your_key_here"

# 4. Install dependencies
pip install -r missions/mission-01/start/requirements.txt
```

## 📂 Case Files

| Badge | ID | Title | Tech Stack | Difficulty | Status |
| :---: | :--- | :--- | :--- | :--- | :--- |
| <img src="assets/badge_l100_bronze.png" width="50"/> | **001** | [The Informant](missions/mission-01/) | Gemini CLI, Python | ⭐ | **OPEN** |
| <img src="assets/badge_l200_silver.png" width="50"/> | **002** | [The Safehouse](missions/mission-02/) | Cloud Run | ⭐⭐ | **OPEN** |
| <img src="assets/object_database_terminal.png" width="50"/> | **003** | [Total Recall](missions/mission-03/) | Cloud SQL, RAG | ⭐⭐⭐ | **OPEN** |

---
*Property of the Cloud Bureau of Investigation. Unauthorized access will be logged.*