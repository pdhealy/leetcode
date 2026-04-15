# 3. Longest Substring Without Repeating Characters

from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    # s = "abcabcbb"
    # Output: 3

    # Example 2:
    # s = "bbbbb"
    # Output: 1

    # Example 3:
    s = "pwwkew"
    # Output: 3
    
    output = solution.lengthOfLongestSubstring(s)
    print(f"The length of the longest substring without repeating characters in '{s}' is: {output}")