# 283. Move Zeroes

## Space Complexity: O(1) because we are modifying the input array in-place without using any additional data structures. We are only using a constant amount of extra space for the left pointer and the right pointer.
## Time Complexity: O(n) because we are iterating through the array once with the right pointer, and each non-zero element is swapped at most once with the left pointer. Therefore, the overall time complexity is linear with respect to the size of the input array.

from solution import Solution
from typing import List

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