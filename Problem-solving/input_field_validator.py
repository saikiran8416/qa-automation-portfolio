# 5️⃣ input_field_validator.py
"""
📌 Problem: Input Field Validator
👨‍💻 Scenario:
Validate a test input form containing fields for email, age, and name.

🎯 Goal:
Check if fields are valid (email contains '@', age is int > 0, name is not empty)

📥 Input:
Dict with keys 'email', 'age', 'name'
📤 Output:
True/False if all fields are valid
"""

def is_input_valid(data):
    if not data.get("email") or "@" not in data["email"]:
        return False
    if not isinstance(data.get("age"), int) or data["age"] <= 0:
        return False
    if not data.get("name") or not data["name"].strip():
        return False
    return True
