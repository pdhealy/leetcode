# 217: Contains Duplicate

## Difficulty: Easy
## Category: Array, Hash Table
## Link: https://leetcode.com/problems/contains-duplicate/
## Tutorial: https://youtu.be/3OamzN90kPg?si=umGZegEzdvOa--eC

## Solution:

# Import List class from typing module
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset to store unique elements
        hashset = set()

        # Iterate through each number in the input list
        for index, num in enumerate(nums):
            # If the number is already in the hashset, return True
            if num in hashset:
                return True
            # Otherwise, add the number to the hashset
            hashset.add(num)
        # If no duplicates were found, return False
        return False

## Test cases:

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

## Debugging

### Example 1
"""
| watch | 0 | 1 | 2 | 3 |
| :---- | :---- | :---- | :---- | :---- |
| hashset | {1} | {1,2} | {1,2,3} | {1,2,3} |
| n | 1 | 2 | 3 | 1 |
| result | False | False | False | True |
"""

### Example 2:
"""
watch       |1      |2      |3      |4          |
hashset     |{}     |{1,2}  |{1,2,3}|{1,2,3,4}  |
n           |1      |2      |3      |4          |
result      |False  |False  |False  |False      |
"""

### Example 3:
"""
watch       |1      |1      |1      |3      |3      |4      |3      |2      |4      |2      |
hashset     |{}     |{1}    |{1}    |{1,3}  |{1,3}  |{1,3,4}|{1,3,4}|{1,2,3,4}|{1,2,3,4}|{1,2,3,4}|
n           |1      |1      |1      |3      |3      |4      |3      |2      |4      |2      |
result      |False  |True   |True   |True   |True   |True   |True   |True   |True   |True   |
"""