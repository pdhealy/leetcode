class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a set to store the characters in the current window
        charSet: set[str] = set()
        # Use two pointers to represent the current window
        left_ptr: int = 0
        # Initialize the result to store the length of the longest substring
        result: int = 0

        # Iterate through the string using the right pointer
        for right_ptr in range(len(s)):
            # If the character at the right pointer is already in the set, it means we have a duplicate character
            while s[right_ptr] in charSet:
                # Remove the character at the left pointer from the set and move the left pointer to the right
                charSet.remove(s[left_ptr])
                left_ptr += 1
            # If the character at the right pointer is not in the set, add it
            charSet.add(s[right_ptr])
            # Update the result with the maximum length of the current window which is the longest substring without repeating characters
            # `right_ptr - left_ptr + 1` gives the length of the current window
            result = max(result, right_ptr - left_ptr + 1)
        # After iterating through the string, return the result
        return result