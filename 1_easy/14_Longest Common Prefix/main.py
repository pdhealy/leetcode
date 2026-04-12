# 14. Longest Common Prefix

## Solution:

from solution import Solution
from typing import List

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