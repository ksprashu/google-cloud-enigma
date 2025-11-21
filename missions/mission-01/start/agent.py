import os
import sys
from google import genai

# ---------------------------------------------------------
# MISSION 001: THE INFORMANT
# TASK: Fix the "TODO" sections to make the agent work.
# ---------------------------------------------------------

def main():
    # TODO 1: The API Key is missing. Retrieve it from the environment variable 'GEMINI_API_KEY'.
    api_key = "FIX_ME" 
    
    if not api_key or api_key == "FIX_ME":
        print("❌ Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # TODO 2: Create the chat session.
    # Define a 'system_instruction' to give your agent a personality (e.g., "You are a tough detective").
    chat = client.chats.create(
        model="gemini-1.5-flash",
        config=genai.types.GenerateContentConfig(
            system_instruction="You are a helpful assistant." # Change this!
        )
    )

    print("🕵️‍♂️ Agent Vertex is online. (Type 'exit' to quit)")

    while True:
        user_input = input("You: ")
        
        # TODO 3: Implement the exit condition.
        # If the user types 'exit', break the loop.

        try:
            response = chat.send_message(user_input)
            print(f"Agent: {response.text}")
        except Exception as e:
            print(f"❌ Connection Error: {e}")
            break

if __name__ == "__main__":
    main()
