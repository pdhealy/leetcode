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