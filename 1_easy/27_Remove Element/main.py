# 27: Remove Element

from solution import Solution

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    # nums = [3, 2, 2, 3]
    # val = 3
    # Output: 2, nums = [2, 2]

    # Example 2:
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    # Output: 5, nums = [0, 1, 3, 0, 4]

    result = solution.removeElement(nums, val)
    print(f"k: {result}")
    print(f"nums: {nums[:result]}")