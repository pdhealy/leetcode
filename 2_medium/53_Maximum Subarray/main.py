# 53: Maximum Subarray

from solution import Solution

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Output: 6
    # Explanation: The subarray [4,-1,2,1] has the largest sum 6.

    # Example 2:
    # nums = [1]
    # Output: 1
    # Explanation: The subarray [1] has the largest sum 1.

    # Example 3:
    # nums = [5, 4, -1, 7, 8]
    # Output: 23
    # Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

    result = solution.maxSubArray(nums)
    print(f"The maximum subarray sum is: {result}")