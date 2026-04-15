# 167: Two Sum II - Input Array Is Sorted

from solution import Solution
from typing import List

if __name__ == "__main__":

    solution = Solution()

    # numbers = [2, 7, 11, 15] # LeetCode example
    
    numbers = [1, 3, 4, 5, 7, 10, 11] # Neetcode example - more comprehensive
    target = 9

    result = solution.twoSum(numbers, target)
    print(f"The indices of the two numbers that add up to {target} are: {result}")