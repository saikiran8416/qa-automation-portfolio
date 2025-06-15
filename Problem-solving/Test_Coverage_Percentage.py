"""
📌 Problem: Test Coverage Calculator
👨‍💻 Scenario:
You know the total number of modules in a feature and how many have been covered by tests.

🎯 Goal:
Calculate the test coverage percentage.

📥 Input:
- Total modules (int)
- Covered modules (int)

📤 Output:
- Coverage percentage (float with 2 decimals)
"""

def calculate_coverage(total, covered):
    if total == 0:
        return 0.0
    return round((covered / total) * 100, 2)

# Example
if __name__ == "__main__":
    print("Coverage:", calculate_coverage(40, 28), "%")
