# 242: Valid Anagram

## Difficulty: Easy
## Category: String, Hash Table
## Link: https://leetcode.com/problems/valid-anagram

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from collections import Counter

class Solution:
    # Approach 1: Using Hash Maps
    def isAnagram1(self, s: str, t: str) -> bool:
        # Check length first
        if len(s) != len(t):
            # If lengths differ, they cannot be anagrams
            return False
        # Create frequency dictionaries
        countS, countT = {}, {}

        for i in range(len(s)):
            # Count frequency of each character in both strings
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for char in countS:
            # Check if each character in countS has the same frequency in countT
            if countS[char] != countT.get(char, 0):
                # If counts differ for any character, they are not anagrams
                return False
        # If all counts match, they are anagrams
        return True

    # Approach 2: Using Counter from collections
    def isAnagram2(self, s: str, t: str) -> bool:
        # Utilize Counter to count character frequencies and compare
        return Counter(s) == Counter(t)

    # Approach 3: Using built-in sorted function
    def isAnagram3(self, s: str, t: str) -> bool:
        # Sort both strings and compare
        return sorted(s) == sorted(t)

## Test cases:

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