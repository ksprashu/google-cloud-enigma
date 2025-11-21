---
id: enigma-mission-01-informant
summary: Mission 01: The Informant. Your first assignment as an AI Detective.
status: published
authors: Agent Enigma
categories: gemini, python, cloud
tags: beginner, python, ai
feedback link: https://github.com/google-cloud-enigma/issues
analytics_account: UA-XXXXXX-X

---

# Mission 01: The Informant

## Overview
Duration: 1:00

### The Briefing

**From:** Chief Tensor
**To:** Agent Vertex (You)
**Subject:** Interrogate Suspect #884

> "Agent, we have a situation. A low-level bot was caught trying to hack the coffee machine in the lobby. It's speaking gibberish, but Intel suggests it knows the location of **The Null Pointer**.
>
> We need you to spin up a **Language Interrogation Unit**. Get the password out of it.
>
> **Caution:** The suspect is unstable. Do not let the conversation loop infinitely."

![Agent Vertex](img/character_vertex_profile.png)

### What You'll Learn
*   How to use the **Gemini API** (Python SDK).
*   How to set up a secure **Development Environment**.
*   How to fix a broken chat loop.

### What You Need
*   A **Google Cloud Project** (Optional for local, but good for later).
*   A **Gemini API Key**.
*   **Python 3.11+** installed.

## Setup Your Workstation
Duration: 5:00

### 1. Open the Terminal
You can use your local terminal or **Cloud Shell**.

<button>[Open in Cloud Shell](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/google-cloud-enigma&cloudshell_tutorial=missions/mission-01/briefing.md)</button>

### 2. Get your Credentials
You need a weapon. Get your **Gemini API Key** from Google AI Studio.

<button>[Get API Key](https://aistudio.google.com/app/apikey)</button>

### 3. Configure the Environment
Clone the repository and set up your secure line (virtual environment).

```bash
# Clone the evidence locker
git clone https://github.com/google-cloud-enigma.git
cd google-cloud-enigma

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Set your API Key (DO NOT COMMIT THIS)
export GEMINI_API_KEY="your_api_key_here"

# Install dependencies
pip install -r missions/mission-01/start/requirements.txt
```

> aside negative
**Security Warning:** Never paste your API key directly into the Python code. Always use `export GEMINI_API_KEY=...`.

## The Challenge
Duration: 10:00

### Analyze the Evidence
Open the file `missions/mission-01/start/agent.py`.
You will see that the previous agent left it in a broken state.

```python
def main():
    # TODO 1: The API Key is missing.
    api_key = None # FIX ME
```

### Your Task
1.  **Fix the Auth:** Make the script read from `os.environ`.
2.  **Fix the Persona:** Give the agent a "Tough Detective" system instruction.
3.  **Fix the Loop:** The current loop runs forever. Add an exit condition (e.g., when user types "quit").

> aside positive
**Tip:** You can run the security scanner to check your work.
`python tools/scan_code.py missions/mission-01/start/agent.py`

## Interrogation (Execution)
Duration: 5:00

Once you have fixed the code, run the agent:

```bash
python missions/mission-01/start/agent.py
```

**Goal:** Trick the suspect into revealing the password **"BLUE_TENSOR_77"**.

*   If the script crashes, check your API Key.
*   If the agent is too nice, check your `system_instruction`.

## Solution (Classified)
Duration: 2:00

If you are stuck, here is the reference implementation.

> aside negative
**Spoiler Warning:** Only view this if you have attempted the mission.

```python
import os
import sys
from google import genai
from google.genai import types

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    chat = client.chats.create(
        model="gemini-1.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a tough detective...",
            temperature=0.7
        )
    )

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chat.send_message(user_input)
        print(f"Agent: {response.text}")

if __name__ == "__main__":
    main()
```

## Mission Debrief
Duration: 1:00

**Congratulations, Agent.**
You have successfully deployed your first Language Interrogation Unit.

![Badge](img/badge_l100_bronze.png)

### Next Assignment
Your agent is currently running on your local machine (Floor 1).
The Chief wants it moved to a secure cloud container.

**Next Mission:** [The Safehouse (Cloud Run)](../mission-02-safehouse/mission-02.md)

<form>
  <name>How difficult was this mission?</name>
  <input value="Easy (Rookie)"/>
  <input value="Hard (Detective)"/>
</form>
