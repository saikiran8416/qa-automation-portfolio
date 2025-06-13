"""
📌 Problem: Test Name Formatter
👨‍💻 Scenario:
Standardize test case names to follow a lowercase with underscore convention.

🎯 Goal:
Convert names like "LoginTestCase" or "Signup Form Test" to "login_test_case" and "signup_form_test"

📥 Input:
String (test case name)
📤 Output:
Formatted string
"""

def format_test_name(name):
    return name.strip().replace(" ", "_").replace("-", "_").lower()