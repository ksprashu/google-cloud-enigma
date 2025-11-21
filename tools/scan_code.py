import os
import re
import sys

def scan_file(filepath):
    print(f"🔎 Scanning {filepath} for security risks...")
    
    issues = 0
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Check 1: Hardcoded API Keys (Naive Regex for long strings assigned to variables)
    # Matches `key = "AIza..."
    key_pattern = r'["\'](AIza[0-9A-Za-z-_]{35})["\']'
    if re.search(key_pattern, content):
        print("   🚨 CRITICAL: Potential Hardcoded API Key detected!")
        print("      -> Remove the key immediately and use os.environ.get()")
        issues += 1
        
    # Check 2: Check if os.environ is used
    if "os.environ.get" not in content and "os.getenv" not in content:
        print("   ⚠️ WARNING: No environment variable usage detected.")
        print("      -> Are you hardcoding credentials?")
        issues += 1

    if issues == 0:
        print("   ✅ Code looks clean.")
        return True
    else:
        print(f"   ❌ Found {issues} security issues.")
        return False

if __name__ == "__main__":
    target_file = "missions/mission-01/start/agent.py"
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        
    if os.path.exists(target_file):
        scan_file(target_file)
    else:
        print(f"❌ File not found: {target_file}")
