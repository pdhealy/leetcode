from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1

    nums = [100,4,200,1,3,2]
    result = solution.longestConsecutive(nums)
    print(f"Example 1 Result: {result}")

    # Example 2
    # This example will execute the main while loop 2 times, because 0 appears twice in the input list, and 0 is the start of the longest consecutive sequence.

    nums = [0,3,7,2,5,8,4,6,0,1]
    result = solution.longestConsecutive(nums)
    print(f"Example 2 Result: {result}")

    # Example 3

    nums = [1,0,1,2]
    result = solution.longestConsecutive(nums)
    print(f"Example 3 Result: {result}")
