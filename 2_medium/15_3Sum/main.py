from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums = [-1,0,1,2,-1,-4]
    print(f"Example 1: {solution.threeSum(nums)}")
    # Expected Output: [[-1,-1,2],[-1,0,1]]

    # Example 2:
    nums = [0,1,1]
    print(f"Example 2: {solution.threeSum(nums)}")
    # Expected Output: []

    # Example 3:
    nums = [0,0,0]
    print(f"Example 3: {solution.threeSum(nums)}")
    # Expected Output: [[0,0,0]]