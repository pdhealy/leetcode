# 76. Minimum Window Substring

- **Difficulty:** Hard
- **Categories:** Hash Table, String, Sliding Window
- **Link:** https://leetcode.com/problems/minimum-window-substring
- **Tutorial:** 

## **Description:**

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window** substring of `s` such that every character in `t` (**including duplicates**) is included in the window*. If there is no such substring, return the *empty string `""`*.

The testcases will be generated such that the answer is **unique**.

## **Examples:**

**Example 1:**
    **Input:** s = "ADOBECODEBANC", t = "ABC"
    **Output:** "BANC"
    **Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

**Example 2:**
    **Input:** s = "a", t = "a"
    **Output:** "a"
    **Explanation:** The entire string s is the minimum window.

**Example 3:**
    **Input:** s = "a", t = "aa"
    **Output:** ""
    **Explanation:** Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

## **Constraints:**

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 105`
- `s` and `t` consist of uppercase and lowercase English letters.

## **Simplified Explanation**:

Build a hash map of chars in `s` and compare against hash mpa of chars in `t`. If we `have` what we `need` then set `res` to the coordinates of the sliding window, and `resLen` to the size of the window. We then pop from the left, moving `l` to the right, checking if we `have` what we `need`, until we find a smaller subset size or end. (see `Custom Example`)