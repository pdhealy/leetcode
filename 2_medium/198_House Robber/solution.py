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