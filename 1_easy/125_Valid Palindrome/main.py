# 125. Valid Palindrome

## Note: Two Pointers (Opposite Ends) are used to compare characters from both ends of the string, moving towards the center. This approach is efficient for checking palindromes.

from solution import Solution

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