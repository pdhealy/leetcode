# 209. Minimum Size Subarray Sum

from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    # target = 7
    # nums = [2,3,1,2,4,3]
    # assert solution.minSubArrayLen(target, nums) == 2

    # Example 2:
    target = 4
    nums = [1,4,4]

    # Example 3:
    # target = 11
    # nums = [1,1,1,1,1,1,1,1]

    output = solution.minSubArrayLen(target, nums)
    print(f"The minimum size of a contiguous subarray of which the sum is at least {target} is: {output}")