# 11. Container With Most Water

## Difficulty: Medium
## Category: Array, Two Pointers (Opposite Ends)
## Link: https://leetcode.com/problems/container-with-most-water
# Tutorial: https://www.youtube.com/watch?v=UuiTKBwPgAo

## Solution:

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the beginning and end of the array
        left_ptr, right_ptr = 0, len(height) - 1
        # Initialize a variable to keep track of the maximum area found
        max_area = 0

        # Loop until the two pointers meet by moving towards each other
        while left_ptr < right_ptr:
            # Calculate the width between the two pointers
            width = right_ptr - left_ptr
            # Calculate the area formed by the lines at the two pointers and the width
            current_area = min(height[left_ptr], height[right_ptr]) * width
            # Update the maximum area if the current area is larger than the previously recorded maximum area
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line inward to potentially find a taller line
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        # After the loop, max_area will contain the maximum area of water that the container can contain
        return max_area
    
## Test cases:

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    height = [1,8,6,2,5,4,8,3,7]
    # Output: 49
    # Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

    # Example 2:
    # height = [1,1]
    # Output: 1

    output = solution.maxArea(height)
    print(f"Max area of water the container can contain: {output}")