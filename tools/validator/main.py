import argparse
import sys
import os
import importlib.util
import urllib.request
import subprocess
from typing import List

def check_env_vars(required_vars: List[str]) -> bool:
    missing = [v for v in required_vars if not os.environ.get(v)]
    if missing:
        print(f"❌ Missing Environment Variables: {', '.join(missing)}")
        return False
    print(f"✅ Environment Variables: OK")
    return True

def check_file_exists(filepath: str) -> bool:
    if not os.path.exists(filepath):
        print(f"❌ Missing File: {filepath}")
        return False
    return True

def run_mission_01_check():
    print("\n🕵️‍♂️ Mission 01 Validation: The Informant")
    if not check_env_vars(["GEMINI_API_KEY"]):
        return False
    agent_path = "missions/mission-01/start/agent.py"
    if not check_file_exists(agent_path):
        return False
    with open(agent_path, 'r') as f:
        content = f.read()
        if 'api_key = "FIX_ME"' in content or 'api_key = None' in content:
             print("❌ Static Check: API Key logic still looks broken. Did you replace the placeholder?")
             return False
    print("✅ Mission 01: Code Structure looks good. Try running it!")
    return True

def run_mission_02_check(url: str):
    print("\n🕵️‍♂️ Mission 02 Validation: The Safehouse")
    if not url:
        print("❌ Error: --url is required for Mission 02 validation.")
        return False
    
    print(f"📡 Pinging {url}...")
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            if "Agent Vertex" in html or "Hello" in html:
                print("✅ Service is responding correctly!")
                return True
            else:
                print(f"⚠️ Service responded, but output was unexpected: {html[:100]}...")
                return False
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
        return False

def run_mission_03_check(instance: str):
    print("\n🕵️‍♂️ Mission 03 Validation: Total Recall")
    if not instance:
        print("❌ Error: --instance is required for Mission 03 validation.")
        return False
    
    print(f"🔎 Checking Cloud SQL Instance: {instance}...")
    try:
        # Use gcloud to check status
        result = subprocess.run(
            ["gcloud", "sql", "instances", "describe", instance, "--format=value(state)"],
            capture_output=True, text=True
        )
        status = result.stdout.strip()
        if status == "RUNNABLE":
            print("✅ Database is RUNNABLE.")
            return True
        else:
            print(f"❌ Database status is: {status} (Expected: RUNNABLE)")
            return False
    except FileNotFoundError:
        print("❌ gcloud CLI not found.")
        return False
    except Exception as e:
        print(f"❌ Error checking database: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Project Enigma Validator")
    parser.add_argument("--mission", type=int, choices=[1, 2, 3], help="Mission number to validate")
    parser.add_argument("--url", type=str, help="Cloud Run URL (Mission 02)")
    parser.add_argument("--instance", type=str, help="Cloud SQL Instance Name (Mission 03)")
    
    args = parser.parse_args()

    if args.mission == 1:
        run_mission_01_check()
    elif args.mission == 2:
        run_mission_02_check(args.url)
    elif args.mission == 3:
        run_mission_03_check(args.instance)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
