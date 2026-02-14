# 121: Best Time to Buy and Sell Stock

# Difficulty: Easy
# Category: Array, Dynamic Programming, Sliding Window
## Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
## Tutorial: https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvn

## Approach: Single Pass Tracking Minimum Price
## Time complexity: O(n)
## Space complexity: O(1)

## Solution:

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

## Test cases:

if __name__ == "__main__":

    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    
    result = solution.maxProfit(prices)
    print(f"Maximum Profit: {result}") # Output: 5