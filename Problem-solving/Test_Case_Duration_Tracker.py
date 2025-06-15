"""
📌 Problem: Test Case Duration Tracker
👨‍💻 Scenario:
You receive a list of test case names with their execution durations in seconds.
You want to track which test cases took longer than a given threshold.

🎯 Goal:
Filter out test cases that took more time than allowed.

📥 Input:
- List of tuples: (test_name, duration_in_seconds)
- Threshold duration (int)

📤 Output:
- List of test names exceeding the threshold
"""

def slow_tests(test_durations, threshold):
    return [name for name, duration in test_durations if duration > threshold]

# Example
if __name__ == "__main__":
    tests = [("LoginTest", 4), ("SignupFlow", 12), ("Checkout", 7)]
    print("Slow tests:", slow_tests(tests, threshold=5))
