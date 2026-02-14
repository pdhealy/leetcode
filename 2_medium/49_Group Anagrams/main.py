# 49. Group Anagrams

## Difficulty: Medium
## Category: Hash Table, String
## Link: https://leetcode.com/problems/group-anagrams/
## Tutorial: https://www.youtube.com/watch?v=vzdNOK2oB2E
## Space Complexity: O(NK) where N is the number of strings in the input list and K is the maximum length of a string in the input list. This is because we are storing all the strings in the output list and each string can have a maximum length of K.
## Time Complexity: O(NK) where N is the number of strings in the input list and K is the maximum length of a string in the input list. This is because we are iterating through each string in the input list and for each string, we are counting the frequency of each character which takes O(K) time. Additionally, we are also iterating through the count array to create a key for the dictionary which also takes O(K) time. Therefore, the overall time complexity is O(NK).


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