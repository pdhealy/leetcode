# 26. Remove Duplicates from Sorted Array

## Difficulty: Easy
## Category: Array, Two Pointers
## Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
## Tutorial: https://youtu.be/DEJAZBq0FDA?si=tweeolVOKlasxTCm

## Solution:

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize the left pointer to 1 since the first element is always unique
        left_ptr = 1

        # Iterate through the array with the right pointer starting from the second element
        for right_ptr in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[right_ptr] != nums[right_ptr - 1]:
                # Update the position at left pointer and increment it
                nums[left_ptr] = nums[right_ptr]
                # Increment the left pointer to the next position
                left_ptr += 1
        # Return the length of the array with unique elements
        return left_ptr

## Test cases:

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    # nums = [1,1,2]
    # Output: 2, nums = [1,2,_]
    # Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

    # Example 2:
    nums = [0,0,1,1,1,2,2,3,3,4]
    # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    # Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.It does not matter what you leave beyond the returned k (hence they are underscores).

    result = solution.removeDuplicates(nums)
    print(f"Result: {result}")