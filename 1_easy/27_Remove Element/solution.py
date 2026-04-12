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

