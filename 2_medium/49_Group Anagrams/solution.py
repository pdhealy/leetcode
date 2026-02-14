# 49. Group Anagrams

from typing import List
from collections import defaultdict

class Solution:
    # Advanced Solution: Using a count array to group anagrams together. The count array is used as a key in the dictionary to group anagrams together. This approach is more efficient than sorting each string because it takes O(K) time to create the count array for each string, whereas sorting takes O(K log K) time. Additionally, using a count array allows us to handle cases where the input strings contain characters that are not in the English alphabet.
    def groupAnagrams_complex(self, strs: List[str]) -> List[List[str]]:
        # Initialize a default dictionary to hold lists of anagrams
        result = defaultdict(list) # mapping charCount to list of Anagrams

        # Iterate through each string in the input list
        for string in strs:
            # Create a count array for each character in the string. The array has 26 elements, one for each letter of the English alphabet.
            count = [0] * 26 # a ... z

            # Count the frequency of each character in the string
            for char in string:
                # Increment the count for the character
                count[ord(char) - ord("a")] += 1

            # Use the count array as a key to group anagrams together
            result[tuple(count)].append(string)

        # Return the grouped anagrams as a list of lists
        return list(result.values())

    def groupAnagrams_fast(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            ans[key].append(string)

        return list(ans.values())