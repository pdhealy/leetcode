# 125. Valid Palindrome

## Difficulty: Easy
## Category: String, Two Pointers (Opposite Ends)
## Link: https://leetcode.com/problems/valid-palindrome
## Tutorial: https://www.youtube.com/watch?v=jJXJ16kPFWg
## Note: Two Pointers (Opposite Ends) are used to compare characters from both ends of the string, moving towards the center. This approach is efficient for checking palindromes.

## Solution:

class Solution:
    # Solution 1: Short, using extra space and built-in functions
    def isPalindromeShort(self, s: str) -> bool:
        # Initialize an empty string to store the cleaned version of the input string
        new_str = ""

        # Iterate through each character in the input string
        for char in s:
            # Check if the character is alphanumeric (either a letter or a digit) using the isalnum() method
            if char.isalnum():
                # If the character is alphanumeric, convert it to lowercase and append it to new_str
                new_str += char.lower()
        # Check if new_str is equal to its reverse (new_str[::-1]) and return the result
        return new_str == new_str[::-1]
    
    # Solution 2: Long, using Two Pointers (Opposite Ends)
    def isPalindromeLong(self, s: str) -> bool:
        # Initialize two pointers, left_ptr at the beginning of the string and right_ptr at the end of the string
        left_ptr, right_ptr = 0, len(s) -1

        # Use a while loop to continue until the left pointer is less than the right pointer
        while left_ptr < right_ptr:
            # Move the left pointer to the right until it points to an alphanumeric character or crosses the right pointer
            while left_ptr < right_ptr and not self.alphaNum(s[left_ptr]):
                left_ptr += 1
            # Move the right pointer to the left until it points to an alphanumeric character or crosses the left pointer
            while right_ptr > left_ptr and not self.alphaNum(s[right_ptr]):
                right_ptr -= 1
            # Compare the characters at the left and right pointers (ignoring case) and return False if they are not equal
            if s[left_ptr].lower() != s[right_ptr].lower():
                return False
            # Move both pointers towards the center for the next comparison
            left_ptr, right_ptr = left_ptr + 1, right_ptr - 1
        # If the loop completes without finding any mismatches, return True, indicating that the string is a valid palindrome
        return True
    
    def alphaNum(self, char):
        # Check if the character is an uppercase letter, a lowercase letter, or a digit by comparing its ASCII value using the ord() function
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

## Test cases:

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    # s = "A man, a plan, a canal: Panama"
    # Output: true
    # Explanation: "amanaplanacanalpanama" is a palindrome.

    # Example 2:
    s = "race a car"
    # Output: false
    # Explanation: "raceacar" is not a palindrome.

    # Example 3:
    # s = " "
    # Output: true
    # Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

    # Solution 1: Short, using extra space and built-in functions
    # output = solution.isPalindromeShort(s)

    # Solution 2: Long, using Two Pointers (Opposite Ends)
    output = solution.isPalindromeLong(s)

    if output:
        print(f"The string '{s}' is a valid palindrome.")
    else:
        print(f"The string '{s}' is not a valid palindrome.")