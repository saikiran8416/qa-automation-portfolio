"""
📌 Problem: Test Result Summary Counter
👨‍💻 Scenario:
Summarize number of passed and failed tests from a list.

🎯 Goal:
Count how many "Passed" and "Failed" entries are in the results.

📥 Input:
List of test result strings ("Passed", "Failed")
📤 Output:
Dictionary with counts
"""

def count_test_status(results):
    summary = {"Passed": 0, "Failed": 0}
    for r in results:
        if r in summary:
            summary[r] += 1
    return summary