# 151. Reverse Words in a String

## Difficulty: Medium
## Category: String, Two Pointers
## Link: https://leetcode.com/problems/reverse-words-in-a-string/
## Tutorial: https://www.youtube.com/watch?v=QjYqgP9i
## Time Complexity: O(n) because we need to iterate through the string once to identify the words and then join them together. The overall time complexity is linear with respect to the size of the input string.
## Space Complexity: O(n) because we are using a deque to store the words in reverse order, and the space required for the deque is proportional to the number of words in the input string. Additionally, the space required for the output string is also proportional to the size of the input string, since we are creating a new string to hold the reversed words. Therefore, the overall space complexity is linear with respect to the size of the input string.

## Solution:

import collections

class Solution:
    # Complex version without using built-in functions
    def reverseWords(self, s: str) -> str:
        # Using deque to efficiently append words to the front of the list
        string_builder: collections.deque[str] = collections.deque()
        # Initialize start to -1 to indicate that we haven't found the start of a word yet
        start: int = -1
        # Initialize i to 0 to start iterating through the string from the beginning
        i: int = 0

        # Iterate through the string until we reach the end
        while i < len(s):
            # If the current character is not a space, it means we have found the start of a word
            if s[i] != " ":
                start = i

                # Continue iterating until we find the end of the word (which is indicated by a space or the end of the string)
                while i < len(s) and s[i] != " ":
                    i += 1
                # Append the word to the front of the deque
                string_builder.appendleft(s[start: i]) 
                # Move the index back by one to account for the extra increment in the inner loop, and then move it forward again to continue iterating through the string
                i -= 1
            i += 1

        return " ".join(string_builder)
    
    def reverseWords_short(self, s: str) -> str:
        # Step 1: Trim leading and trailing spaces and split the string into words
        words: list[str] = s.strip().split()
        
        # Step 2: Reverse the list of words
        words.reverse()
        
        # Step 3: Join the reversed list of words with a single space and return the result
        return ' '.join(words)

## Test cases:

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    # s = "the sky is blue"
    # Output: "blue is sky the"

    # Example 2:
    s = "  hello world  "
    # Output: "world hello"
    # Explanation: Your reversed string should not contain leading or trailing spaces.

    # Example 3:
    # s = "a good   example"
    # Output: "example good a"
    # Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

    # output = solution.reverseWords(s)

    output = solution.reverseWords_short(s)
    print(output)