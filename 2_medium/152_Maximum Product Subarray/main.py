# 152. Maximum Product Subarray

## Difficulty: Medium
## Category: Array, Dynamic Programming
## https://leetcode.com/problems/maximum-product-subarray
## Tutorial: https://www.youtube.com/watch?v=lXVy6YWFcRM

## Solution:

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize result with the maximum number in the array to handle cases where all numbers are negative or zero, ensuring we return the correct maximum product even if it's a single element
        result = max(nums)
        # Initialize current minimum and maximum product to 1 so that they don't affect the product calculation initially (i.e., 1 is the multiplicative identity)
        curMin, curMax = 1, 1

        for n in nums:
            # Edge case: reset when n is 0 because any product involving 0 will be 0, and we need to start fresh for the next subarray
            if n == 0:
                # Reset current min and max product
                curMin, curMax = 1, 1
                # Guard Clause to reduce indentation below
                continue

            # Store current max before updating it to use for curMin calculation
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            # Update result with the maximum product found so far
            result = max(result, curMax)

        return result

## Test cases:

if __name__ == "__main__":
    
    solution = Solution()

    # Example 1:
    # nums = [2, 3, -2, 4]
    # Output: 6
    # Explanation: [2,3] has the largest product 6.

    # Example 2:
        # nums = [-2,0,-1]
    # Output: 0
    # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

    # Example 3 - Custom:
    nums = [-2, 3, -4]
    # Output: 24
    # Explanation: The subarray [-2,3,-4] has the largest product 24.

    output = solution.maxProduct(nums)
    print(f"Maximum product subarray of {nums} is {output}")