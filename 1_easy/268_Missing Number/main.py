# 268. Missing Number

from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums = [3, 0, 1]
    print(f'Example 1 Result: {solution.missingNumber(nums)}') # Output: 2

    # Example 2:
    nums = [0, 1]
    print(f'Example 2 Result: {solution.missingNumber(nums)}') # Output: 2

    # Example 3:
    nums = [9,6,4,2,3,5,7,0,1]
    print(f'Example 3 Result: {solution.missingNumber(nums)}') # Output: 8