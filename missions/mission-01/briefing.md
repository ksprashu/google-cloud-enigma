# 📁 CASE FILE #001: THE INFORMANT

**Clearance:** L100 (Rookie)
**Location:** Floor 1 (The Lobby)

![Agent Vertex](assets/character_vertex_profile.png)

## 🕵️‍♂️ Mission Briefing
**From:** Chief Tensor
**To:** Agent Vertex (You)
**Subject:** Interrogate Suspect #884

> "Agent, we have a situation. A low-level bot was caught trying to hack the coffee machine in the lobby. It's speaking gibberish, but Intel suggests it knows the location of **The Null Pointer**.
>
> We need you to spin up a **Language Interrogation Unit**. Get the password out of it.
>
> **Caution:** The suspect is unstable. Do not let the conversation loop infinitely."

## 🎯 Objectives
1.  **Configure:** Set up your `gemini-cli` environment.
2.  **Persona:** Define the System Instructions for your Interrogator Agent (You can be "Good Cop" or "Bad Cop").
3.  **Code:** Fix the broken chat loop in `agent.py`.
4.  **Extract:** Trick the suspect into revealing the password: `BLUE_TENSOR_77`.

## 🛠️ The Toolkit
*   **Tech:** Python 3.11+, Google GenAI SDK (`google-genai`).
*   **Model:** `gemini-1.5-flash` (Fast, efficient).

## 🚀 Start Your Investigation
1.  Open the folder `missions/mission-01/start/`.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Run the agent: `python agent.py`.
    *   *Observation:* It crashes. It's missing the API Key and the loop logic is flawed.
4.  **Your Task:** Fix `agent.py` until you can have a conversation.

## 🆘 Hints
<details>
<summary>How do I set the API Key?</summary>
You need to export it in your terminal:
<code>export GEMINI_API_KEY="your_key_here"</code>
</details>

<details>
<summary>The loop keeps crashing</summary>
Ensure you have a <code>break</code> condition when the user says "exit" or "quit".
</details>
