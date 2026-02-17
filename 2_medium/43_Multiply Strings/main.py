# 43. Multiply Strings

## Difficulty: Medium
## Category: String, Math
## Link: https://leetcode.com/problems/multiply-strings
## Tutorial: https://www.youtube.com/watch?v=1vZswirL8Y8

from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    num1 = "2"
    num2 = "3"
    # Output: "6"

    # Example 2:
    # num1 = "123"
    # num2 = "456"
    # Output: "56088"

    # Example: Custom
    # num1 = "12"
    # num2 = "34"
    # Output: "408"

    output = solution.multiply(num1, num2)
    print(f"The product of '{num1}' and '{num2}' is: {output}")