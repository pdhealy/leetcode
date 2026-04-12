# 121: Best Time to Buy and Sell Stock

# Difficulty: Easy
# Category: Array, Dynamic Programming, Sliding Window
## Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
## Tutorial: https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvn

## Approach: Single Pass Tracking Minimum Price
## Time complexity: O(n)
## Space complexity: O(1)

## Solution:



from solution import Solution
from typing import List

if __name__ == "__main__":

    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    
    result = solution.maxProfit(prices)
    print(f"Maximum Profit: {result}") # Output: 5