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