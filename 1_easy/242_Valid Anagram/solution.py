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