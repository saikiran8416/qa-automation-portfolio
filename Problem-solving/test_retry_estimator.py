# 3️⃣ test_retry_estimator.py
"""
📌 Problem: Test Retry Estimator
👨‍💻 Scenario:
If a test fails, it is retried a fixed number of times. Estimate the total retry attempts needed.

🎯 Goal:
Given a list of test results and max retry limit, estimate retry attempts.

📥 Input:
- List of test outcomes ("Passed" or "Failed")
- Retry limit (int)
📤 Output:
Total retry attempts needed to eventually pass or exhaust retries.
"""

def estimate_retries(results, retry_limit):
    retries = 0
    for result in results:
        if result == "Failed":
            retries += retry_limit
    return retries