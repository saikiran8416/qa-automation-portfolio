# 2️⃣ flaky_test_counter.py
"""
📌 Problem: Flaky Test Counter
👨‍💻 Scenario:
A flaky test fails sometimes and passes other times. We want to count such tests.

🎯 Goal:
Identify test cases that failed at least once and passed at least once.

📥 Input:
List of (test_name, status) where status is "Passed" or "Failed"
📤 Output:
List of flaky test names
"""

def find_flaky_tests(logs):
    test_map = {}
    for name, status in logs:
        if name not in test_map:
            test_map[name] = set()
        test_map[name].add(status)
    return [name for name, statuses in test_map.items() if "Passed" in statuses and "Failed" in statuses]
