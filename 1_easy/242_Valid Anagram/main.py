# 242: Valid Anagram

## Difficulty: Easy
## Category: String, Hash Table
## Link: https://leetcode.com/problems/valid-anagram

from solution import Solution
from collections import Counter

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram1(s, t)
    print(f"Is '{t}' an anagram of '{s}'? {result}")
    
    # Example 2:
    s2 = "rat"
    t2 = "car"
    result2 = solution.isAnagram1(s2, t2)
    print(f"Is '{t2}' an anagram of '{s2}'? {result2}")