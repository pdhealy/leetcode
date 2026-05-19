from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    nums = [4,5,6,7,0,1,2]
    target = 0
    print(f"Index of target {target}: {solution.search(nums, target)}")  # Output: 4

    # Example 2:

    nums = [4,5,6,7,0,1,2]
    target = 3
    print(f"Index of target {target}: {solution.search(nums, target)}")  # Output: -1

    # Example 3:

    nums = [1]
    target = 0
    print(f"Index of target {target}: {solution.search(nums, target)}")  # Output: -1

    # Custom Example 1:

    nums = [4,5,6,7,0,1,2]
    target = 6
    print(f"Index of target {target}: {solution.search(nums, target)}")  # Output: 2

    # Custom Example 2:

    nums = [6,7,8,0,1,2,3,4,5]
    target = 8
    print(f"Index of target {target}: {solution.search(nums, target)}")  # Output: 2