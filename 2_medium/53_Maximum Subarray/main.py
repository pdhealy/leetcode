# 53: Maximum Subarray

## Difficulty: Medium
## Category: Array, Dynamic Programming, Divide and Conquer
## Link: https://leetcode.com/problems/maximum-subarray/
## Tutorial: https://www.youtube.com/watch?v=5WZl3MMT0

## Time complexity: O(n)
## Space complexity: O(1)

## Solution: Kadane's Algorithm

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxSubSum to the first element of the array and currentSum to 0
        maxSubSum = nums[0]
        currentSum = 0

        for num in nums:
            
            # If currentSum drops below 0, reset it to 0
            if currentSum < 0:
                currentSum = 0
            
            # If currentSum is non-negative, add the current number
            currentSum += num
            
            # Update maxSubSum if currentSum is greater
            maxSubSum = max(maxSubSum, currentSum)

        return maxSubSum

## Test cases:

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Output: 6
    # Explanation: The subarray [4,-1,2,1] has the largest sum 6.

    # Example 2:
    # nums = [1]
    # Output: 1
    # Explanation: The subarray [1] has the largest sum 1.

    # Example 3:
    # nums = [5, 4, -1, 7, 8]
    # Output: 23
    # Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

    result = solution.maxSubArray(nums)
    print(f"The maximum subarray sum is: {result}")