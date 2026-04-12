from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize two pointers
        left_ptr, right_ptr = 0, 1
        # Initialize maxProfit to keep track of the maximum profit
        maxProfit = 0

        # Traverse through the prices array until the right pointer reaches the end
        while right_ptr < len(prices):

            # If the price at left pointer is less than the price at right pointer then calculate profit
            if prices[left_ptr] < prices[right_ptr]:
                # Calculate profit
                profit = prices[right_ptr] - prices[left_ptr]
                # Update maxProfit if the current profit is greater
                maxProfit = max(maxProfit, profit)
            else:
                # Move left pointer to right if the right price is less than or equal to left price
                left_ptr = right_ptr
            
            # Move right pointer to the next position besides left
            right_ptr += 1

        return maxProfit