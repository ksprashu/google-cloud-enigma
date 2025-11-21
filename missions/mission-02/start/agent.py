import os
import sys
from google import genai

# ---------------------------------------------------------
# MISSION 002: THE SAFEHOUSE
# This is the working agent from Mission 01.
# Your task is NOT to change this file, but to Dockerize it.
# ---------------------------------------------------------

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    
    print("🕵️‍♂️ Agent Vertex Container Initialized.")
    print("📝 Running diagnostics...")
    
    # Simple test for the container logs
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents="Hello from inside a Google Cloud Run container!"
        )
        print(f"🤖 Gemini Response: {response.text}")
        print("✅ System Status: OPERATIONAL")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
