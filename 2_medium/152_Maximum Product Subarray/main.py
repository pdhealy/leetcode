# 152. Maximum Product Subarray

from solution import Solution

if __name__ == "__main__":
    
    solution = Solution()

    # Example 1:
    # nums = [2, 3, -2, 4]
    # Output: 6
    # Explanation: [2,3] has the largest product 6.

    # Example 2:
        # nums = [-2,0,-1]
    # Output: 0
    # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

    # Example 3 - Custom:
    nums = [-2, 3, -4]
    # Output: 24
    # Explanation: The subarray [-2,3,-4] has the largest product 24.

    output = solution.maxProduct(nums)
    print(f"Maximum product subarray of {nums} is {output}")