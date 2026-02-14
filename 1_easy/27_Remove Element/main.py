# 27: Remove Element

## Difficulty: Easy
## Category: Array, Two Pointers
## Link: https://leetcode.com/problems/remove-element/
## Tutorial: https://youtu.be/Pcd1ii9P9ZI?si=MIRUjFFAQkxwqK2A

## Solution:

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for the position of the next non-val element
        k_ptr: int = 0

        # Iterate through the indices of the array
        for i in range(len(nums)):
            # If the current element is not equal to val, we keep it
            if nums[i] != val:
                # Move the non-val element to the front of the array
                nums[k_ptr] = nums[i]
                # Increment the position for the next non-val element
                k_ptr += 1
        # Return the new length of the array without val elements
        return k_ptr

## Test cases:

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