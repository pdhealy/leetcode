# 283. Move Zeroes

from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        """
        No return value required. Modify nums in-place instead.
        """
        # Initialize the left pointer to keep track of the position to place the next non-zero element
        left_ptr = 0

        # Iterate through the array with the right pointer
        for right_ptr in range(len(nums)):
            # If the current element is non-zero, swap it with the element at the left pointer and move the left pointer forward
            if nums[right_ptr]:
                # Swap the non-zero element at right_ptr with the element at left_ptr
                nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
                # Move the left pointer to the next position
                left_ptr += 1
        # The left pointer will have moved all non-zero elements to the front of the array, and the remaining elements will be zeroes.
        return nums # type: ignore