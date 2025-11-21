import os
import sys
from google import genai
from google.genai import types

def main():
    # 1. Get API Key securely
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # 2. Define Persona
    # "Bad Cop" persona to intimidate the suspect.
    persona = """
    You are Detective Vertex. You are tough, impatient, and cybernetically enhanced.
    You are interrogating a suspect. Keep your answers short and punchy.
    Do not reveal classified info easily.
    """

    chat = client.chats.create(
        model="gemini-1.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=persona,
            temperature=0.7
        )
    )

    print("🕵️‍♂️ Agent Vertex is online. (Type 'exit' to quit)")

    # 3. The Chat Loop
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Agent: *Disconnecting uplink...*")
                break
                
            response = chat.send_message(user_input)
            print(f"Agent: {response.text}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            break

if __name__ == "__main__":
    main()
