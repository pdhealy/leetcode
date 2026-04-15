# 125. Valid Palindrome

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