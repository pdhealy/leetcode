# 49. Group Anagrams

from solution import Solution

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
    
    output = solution.groupAnagrams_complex(strs)  # Insert breakpoint here and start debugging
    output = solution.groupAnagrams_fast(strs)  # Insert breakpoint here and start debugging

    print(output)