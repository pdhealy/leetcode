# Leetcode Problem 198: House Robber
## Link: https://leetcode.com/problems/house-robber/
# Tutorial: https://www.youtube.com/watch?v=73r3KWiEvyk&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=10

# Category: Medium
# Problem Type: Dynamic Programming
# Approach: Dynamic Programming - Bottom Up
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        # rob1 = max amount robbed till the house before the previous house
        # rob2 = max amount robbed till the previous house
        for n in nums:
            # Current max rob amount
            temp = max(n + rob1, rob2)
            # Update rob1 and rob2 for next iteration
            rob1 = rob2
            # Set rob2 to the new maximum amount
            rob2 = temp
        return rob2
    
## Test cases:
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    result = solution.rob(nums)
    print(f"The maximum amount that can be robbed is: {result}")

# Example Walkthrough
"""
With nums = [2, 7, 9, 3, 1]:

Initial: rob1=0, rob2=0

House 2: max(2+0, 0) = 2  → rob1=0, rob2=2
House 7: max(7+0, 2) = 7  → rob1=2, rob2=7
House 9: max(9+2, 7) = 11 → rob1=7, rob2=11
House 3: max(3+7, 11) = 11 → rob1=11, rob2=11
House 1: max(1+11, 11) = 12 → rob1=11, rob2=12

Answer: 12 (rob houses: 2, 9, 1)
"""