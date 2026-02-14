# 14. Longest Common Prefix

## Difficulty: Easy
## Category: String
## Link: https://leetcode.com/problems/longest-common-prefix/
## Tutorial: https://www.youtube.com/watch?v=0sWShKIJoo4

## Solution:

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

if __name__ == "__main__":
    
    solution = Solution()

    # Example 1:
    strs = ["flower", "flow", "flight"]
    # Output: "fl"

    # Example 2:
    # strs = ["dog", "racecar", "car"]
    # Output: ""

    result = solution.longestCommonPrefix(strs)
    # If the result is an empty string, it means there is no common prefix found among the input strings.
    if not result:
        print("No common prefix found.")
    # Otherwise, it will print the longest common prefix.
    else:
        print(f"Longest common prefix is: {result}")