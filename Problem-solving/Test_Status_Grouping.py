"""
📌 Problem: Test Status Grouping
👨‍💻 Scenario:
After test execution, you want to group test names by their status.

🎯 Goal:
Return a dictionary where keys are "Passed", "Failed", etc. and values are lists of test names.

📥 Input:
- List of tuples: (test_name, status)

📤 Output:
- Dictionary with grouped test names
"""

def group_tests_by_status(results):
    grouped = {}
    for name, status in results:
        grouped.setdefault(status, []).append(name)
    return grouped

# Example
if __name__ == "__main__":
    test_results = [("Login", "Passed"), ("Signup", "Failed"), ("Search", "Passed")]
    print("Grouped Tests:", group_tests_by_status(test_results))
