from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    s = "ABAB"
    k = 2

    print(f"Example 1: {solution.characterReplacement(s, k)}")

    # Example 2:

    s = "AABABBA"
    k = 1

    print(f"Example 2: {solution.characterReplacement(s, k)}")