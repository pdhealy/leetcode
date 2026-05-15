# 347. Top K Frequent Elements

- **Difficulty:** Medium
- **Categories:** Array, Hash Table, Sorting, Divide and Conquer, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
- **Link:** https://leetcode.com/problems/top-k-frequent-elements
- **Tutorial:** 

## **Description:**

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

## **Examples:**

**Example 1:**
    **Input:** nums = [1,1,1,2,2,3], k = 2
    **Output:** [1,2]

**Example 2:**
    **Input:** nums = [1], k = 1
    **Output:** [1]

**Example 3:**
    **Input:** [1,2,1,2,1,2,3,1,3,2], k = 2
    **Output:** [1,2]
    **Explanation:** n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

## **Constraints:**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.