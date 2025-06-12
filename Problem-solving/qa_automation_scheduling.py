"""
📌 Problem: Test Execution Window Optimization
👨‍💻 Real-World QA Scenario:
As a QA Automation Engineer, you often schedule automated test suites on limited test environments.
Each test suite takes a time slot (start_time, end_time), and **no two suites can run simultaneously** on the same machine.

🎯 Goal:
Given a list of test executions represented by their start and end times, find the **maximum number of test cases** you can schedule **without overlapping**, to optimize usage of limited test devices.

🔍 Why This Matters:
This helps improve parallel execution planning in CI/CD pipelines or when managing physical test labs where devices are shared.

📥 Input:
A list of tuples, each tuple contains:
(start_time: int, end_time: int)

📤 Output:
An integer – the maximum number of non-overlapping test cases that can be run.

🧪 Example:
Input:
    [(0, 30), (5, 10), (15, 20), (35, 50)]
Output:
    3
Explanation:
    - We can run (5, 10), (15, 20), (35, 50)
    - These do not overlap.
"""


def max_non_overlapping_tests(test_suites):

    # Sort by end time (greedy strategy)
    test_suites.sort(key=lambda x: x[1])

    count = 0
    last_end_time = -1

    for start, end in test_suites:
        if start >= last_end_time:
            count += 1
            last_end_time = end

    return count


# Example usage
if __name__ == "__main__":
    tests = [(0, 30), (5, 10), (15, 20), (35, 50)]
    result = max_non_overlapping_tests(tests)
    print("✅ Max non-overlapping test runs:", result)
