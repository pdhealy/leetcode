# 217: Contains Duplicate

## Difficulty: Easy
## Category: Array, Hash Table
## Link: https://leetcode.com/problems/contains-duplicate/
## Tutorial: https://youtu.be/3OamzN90kPg?si=umGZegEzdvOa--eC


from solution import Solution
from typing import List

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    # nums = [1, 2, 3, 1]

    # Example 2:
    # nums = [1, 2, 3, 4]

    # Example 3:
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    result = solution.containsDuplicate(nums)
     # Output will be True or False based on the input list
    print(f"Contains Duplicate: {result}")