# 560. Subarray Sum Equals K

from solution import Solution

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    # nums = [1, 1, 1]
    # k = 2
    # Output: 2

    # Example 2:
    # nums = [1, 2, 3]
    # k = 3
    # Output: 2

    # Example 3: Custom
    nums = [1, 2, -1, 3]
    k = 3
    # Output: 2

    output = solution.subarraySum(nums, k)
    print(f"The number of subarrays that sum to {k} is: {output}")