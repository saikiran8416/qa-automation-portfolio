"""
📌 Problem: Automation Script Name Generator
👨‍💻 Scenario:
You want to auto-generate clean file names for scripts based on a test case title.

🎯 Goal:
Convert a title like "Login Flow with Invalid Data" into a Pythonic script name like "login_flow_with_invalid_data.py"

📥 Input:
- Title string

📤 Output:
- Python file name string
"""

def generate_script_name(title):
    return title.strip().lower().replace(" ", "_") + ".py"

# Example
if __name__ == "__main__":
    print("Script Name:", generate_script_name("Login Flow with Invalid Data"))
