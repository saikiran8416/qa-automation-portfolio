"""
📌 Problem: Duplicate Test Case Checker
👨‍💻 Scenario:
Your QA test plan must not include duplicate test case IDs.

🎯 Goal:
Return True if all test case IDs are unique.

📥 Input:
List of test_case_ids (strings)
📤 Output:
True/False
"""

def are_test_case_ids_unique(test_case_ids):
    return len(set(test_case_ids)) == len(test_case_ids)
