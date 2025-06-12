# 4️⃣ log_error_parser.py
"""
📌 Problem: Error Log Parser
👨‍💻 Scenario:
Extract error messages from QA logs.

🎯 Goal:
Parse multiline logs and return a list of lines that start with "ERROR:"

📥 Input:
Multiline string
📤 Output:
List of error lines
"""

def parse_error_logs(log):
    return [line for line in log.splitlines() if line.strip().startswith("ERROR:")]
