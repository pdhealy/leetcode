# 88: Merge Sorted Array

- Difficulty: Easy
- Topics:
    - Array
    - Two Pointers

## Problem:
You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

## Approach:
Use three pointers from the end:
- i = m - 1 for nums1 valid tail
- j = n - 1 for nums2 tail
- k = m + n - 1 for write position in nums1
Place the larger of nums1[i] and nums2[j] at nums1[k], then move pointers.

## Complexity:
- Time: O(m + n)
- Space: O(1)

## References:
- https://leetcode.com/problems/merge-sorted-array/
- https://www.youtube.com/watch?v=P1Ic85RarKY