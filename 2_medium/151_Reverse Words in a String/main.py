# 151. Reverse Words in a String

from solution import Solution

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