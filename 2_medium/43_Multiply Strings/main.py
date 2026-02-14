# 43. Multiply Strings

## Difficulty: Medium
## Category: String, Math
## Link: https://leetcode.com/problems/multiply-strings
## Tutorial: https://www.youtube.com/watch?v=1vZswirL8Y8

## Solution:

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either of the numbers is "0", the result is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize a list to store the intermediate results of multiplication
        result: list[int] = [0] * (len(num1) + len(num2))

        # Reverse both numbers to facilitate multiplication from the least significant digit
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Multiply each digit of num1 with each digit of num2 and add the results to the appropriate positions in the result list
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Multiply the current digits and add to the existing value at the position (i + j) in the result list
                product = int(num1[i]) * int(num2[j]) + result[i + j]
                result[i + j] = product % 10  # Store the last digit of the product at position (i + j)
                result[i + j + 1] += product // 10  # Add the carry to the next position (i + j + 1)

        # Remove leading zeros from the result list and convert it back to a string
        while len(result) > 1 and result[-1] == 0:
            result.pop()  # Remove trailing zeros from the end of the list

        return ''.join(map(str, result[::-1]))  # Reverse back and convert to string
    
## Test cases:

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    # num1 = "2"
    # num2 = "3"
    # Output: "6"

    # Example 2:
    # num1 = "123"
    # num2 = "456"
    # Output: "56088"

    # Example: Custom
    num1 = "12"
    num2 = "34"
    # Output: "408"

    output = solution.multiply(num1, num2)
    print(f"The product of '{num1}' and '{num2}' is: {output}")