# 238. Product of Array Except Self

## Difficulty: Medium
## Category: Array, Prefix Sum, Suffix Sum
## Link: https://leetcode.com/problems/product-of-array-except-self/description/
## Tutorial: https://www.youtube.com/watch?v=bNvIQI2wAjk

## Solution:

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s to hold the products
        res = [1] * (len(nums))
        # Initialize prefix product to 1 to calculate the product of elements to the left of the current index
        prefix = 1

        # Calculate the product of elements to the left of the current index and store it in the result array
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1

        # Calculate the product of elements to the right of the current index and multiply it with the existing value in the result array
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

## Test cases:

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