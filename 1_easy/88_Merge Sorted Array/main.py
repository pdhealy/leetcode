# 88: Merge Sorted Array

## Difficulty: Easy
## Category: Array, Two Pointers (from the end)
## Link: https://leetcode.com/problems/merge-sorted-array/
## Tutorial: https://www.youtube.com/watch?v=P1Ic85RarKY

## Time complexity: O(m + n)
## Space complexity: O(1)

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Initialize pointer for the last index of nums1
        last = m + n - 1

        # Merge in reverse order
        # m and n need to be greater than 0 to avoid index error
        while m > 0 and n > 0:
            # Move the larger element to the end of nums1 if greater than the last element in nums2
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            # Move the last pointer to the left after placing an element in nums1
            last -= 1

        # This while loop only starts once the first while loop is done, which means that if there are remaining elements in nums2, we need to copy them to nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

## Test cases:

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    # Example 2:
    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0

    # Example 3:
    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1

    solution.merge(nums1, m, nums2, n) # Insert breakpoint here and start debugging
    print(f"Merged Array: {nums1}") # Output: [1, 2, 2, 3, 5, 6]