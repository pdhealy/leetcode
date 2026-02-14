# 283. Move Zeroes

## Difficulty: Easy
## Category: Array, Two Pointers, In-Place Array Manipulation
## Link: https://leetcode.com/problems/move-zeroes/
## Tutorial: https://www.youtube.com/watch?v=aayNRwUN3Do
## Space Complexity: O(1) because we are modifying the input array in-place without using any additional data structures. We are only using a constant amount of extra space for the left pointer and the right pointer.
## Time Complexity: O(n) because we are iterating through the array once with the right pointer, and each non-zero element is swapped at most once with the left pointer. Therefore, the overall time complexity is linear with respect to the size of the input array.

## Solution:

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

## Test cases:

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [0, 1, 0, 3, 12]
    # Output: [1, 3, 12, 0, 0]

    # Example 2:
    # nums = [0]
    # Output: [0]

    output = solution.moveZeros(nums)
    print(output)