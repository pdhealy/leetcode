from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize an empty string to store the result
        result: str = ""
        # Find the maximum length among all strings
        max_len: int = max(len(s) for s in strs)

        # Iterate through each index up to the maximum length
        # for i in range(len(strs[0])): # Original from Neetcode
        for i in range(max_len):
            # Iterate through each string in the list
            for s in strs:

                # If the index exceeds the length of the string or characters don't match the characters at the same index in the first string, return the result
                if i == len(s) or s[i] != strs[0][i]:
                    # Return the result as the longest common prefix found so far
                    return result
                
            # If all strings have the same character at this index, append it to the result
            result += strs[0][i]

        return result

## Test cases:

