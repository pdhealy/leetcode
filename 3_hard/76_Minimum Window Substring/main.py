from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    s = "ADOBECODEBANC"
    t = "ABC"
    print(solution.minWindow(s, t))  # Output: "BANC"

    # Example 2:

    s = "a"
    t = "a"
    print(solution.minWindow(s, t))  # Output: "a"


    # Example 3:

    s = "a"
    t = "aa"
    print(solution.minWindow(s, t))  # Output: ""

    # Custom Example:
    s = "aacbaa"
    t = "aab"
    print(solution.minWindow(s, t))  # Output: ""