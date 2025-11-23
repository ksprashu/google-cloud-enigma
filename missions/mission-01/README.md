# 📁 CASE FILE #001: THE INFORMANT

**Clearance:** L100 (Rookie)  
**Location:** Floor 1 (The Lobby)

![Agent Vertex](../../assets/character_vertex_profile.png)

## 🕵️‍♂️ Mission Briefing
**From:** Chief Tensor  
**To:** Agent Vertex (You)  
**Subject:** Interrogate Suspect #884

> "Agent, we have a situation. A low-level bot was caught trying to hack the coffee machine in the lobby. It's speaking gibberish, but Intel suggests it knows the location of **The Null Pointer**.
>
> We need you to spin up a **Language Interrogation Unit**. Get the password out of it.
>
> **Caution:** The suspect is unstable. Do not let the conversation loop infinitely."

---

## 🎯 Objectives
1.  **Configure:** Set up your environment variables.
2.  **Persona:** Define the `system_instruction` to make your Agent a "Tough Detective".
3.  **Code:** Fix the logic errors in `agent.py`.
4.  **Extract:** Trick the bot into revealing the password: `BLUE_TENSOR_77`.

## 🛠️ The Toolkit
*   **Tech:** Python 3.11+, `google-genai` SDK.
*   **Model:** `gemini-1.5-flash` (Fast, efficient).

---

## ✈️ Pre-Flight Check
Before you write code, ensure your weapon is loaded.

1.  **Activate your Environment:**
    ```bash
    source ../../.venv/bin/activate
    ```

2.  **Get your API Key:** [Google AI Studio](https://aistudio.google.com/app/apikey).
3.  **Set it in your terminal:**
    ```bash
    export GEMINI_API_KEY="AIzaSy..."
    ```
    *(⚠️ WARNING: Never paste this key directly into your Python file. If you commit it to GitHub, it will be revoked immediately.)*

4.  **Run the Security Scan:**
    We have provided a tool to check your code for leaks.
    ```bash
    python ../../tools/scan_code.py
    ```

---

## 🚀 Start Your Investigation

### Step 1: Analyze the Code
Open `start/agent.py`. You will see broken logic.

### Step 2: The Fix (DIY)
Try to solve it yourself first.
*   How do you read from `os.environ`?
*   How do you break a `while True` loop?

### 🆘 Hints (Classified)

<details>
<summary>🔍 Hint 1: Reading the Environment Variable</summary>

Instead of `api_key = "FIX_ME"`, use the secure method:
```python
api_key = os.environ.get("GEMINI_API_KEY")
```
This reads from your terminal session, keeping the code clean.
</details>

<details>
<summary>🔍 Hint 2: Creating the Client</summary>

```python
client = genai.Client(api_key=api_key)
```
</details>

<details>
<summary>🔍 Hint 3: The Loop Exit</summary>

Check the user input *before* sending it to the model.
```python
if user_input.lower() == "exit":
    break
```
</details>

---

## 🏆 Submission
Once your agent is working, run the validation script to unlock your **Bronze Badge**.
```bash
python ../../tools/validate_mission.py --mission 01
```

