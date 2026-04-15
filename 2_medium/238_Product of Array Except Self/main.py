# 238. Product of Array Except Self

from solution import Solution
from typing import List

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [1, 2, 3, 4]
    # Output: [24, 12, 8, 6]

    # Example 2:
    # nums = [-1, 1, 0, -3, 3]
    # Output: [0, 0, 9, 0, 0]
    
    output = solution.productExceptSelf(nums)
    print(f"Product of array except self for {nums} is {output}")