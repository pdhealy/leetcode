# Leetcode Problem 198: House Robber

from solution import Solution

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