# 49. Group Anagrams

## Difficulty: Medium
## Category: Hash Table, String
## Link: https://leetcode.com/problems/group-anagrams/
## Tutorial: https://www.youtube.com/watch?v=vzdNOK2oB2E
## Space Complexity: O(NK) where N is the number of strings in the input list and K is the maximum length of a string in the input list. This is because we are storing all the strings in the output list and each string can have a maximum length of K.
## Time Complexity: O(NK) where N is the number of strings in the input list and K is the maximum length of a string in the input list. This is because we are iterating through each string in the input list and for each string, we are counting the frequency of each character which takes O(K) time. Additionally, we are also iterating through the count array to create a key for the dictionary which also takes O(K) time. Therefore, the overall time complexity is O(NK).

## Solution:

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

## Test cases:

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    # Example 2:
    # strs = [""]
    # Output: [[""]]

    # Example 3:
    # strs = ["a"]
    # Output: [["a"]]
    
    output = solution.groupAnagrams_complex(strs)
    output = solution.groupAnagrams_fast(strs)

    print(output)