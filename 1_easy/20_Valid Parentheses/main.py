from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    s = "()"
    print(solution.isValid(s))

    # Example 2:
    s = "()[]{}"
    print(solution.isValid(s))

    # Example 3:
    s = "(]"
    print(solution.isValid(s))

    # Example 4:
    s = "([])"
    print(solution.isValid(s))

    # Example 5:
    s = "([)]"
    print(solution.isValid(s))