# 27: Remove Element

## Description:
"""
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:
- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.
"""

## Difficulty: Easy
## Category: Array, Two Pointers
## Link: https://leetcode.com/problems/remove-element/
## Tutorial: https://youtu.be/Pcd1ii9P9ZI?si=MIRUjFFAQkxwqK2A

## Solution:



from solution import Solution
from typing import List

if __name__ == "__main__":
    
    solution = Solution()

    # Example 1:
    # nums = [3, 2, 2, 3]
    # val = 3
    # Output: 2, nums = [2, 2]

    # Example 2:
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    # Output: 5, nums = [0, 1, 3, 0, 4]

    result = solution.removeElement(nums, val)
    print(f"k: {result}")
    print(f"nums: {nums[:result]}")