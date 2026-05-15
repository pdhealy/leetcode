from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    nums = [1,1,1,2,2,3]
    k = 2
    print(solution.topKFrequent(nums, k)) # [1, 2]

    # Example 2:

    nums = [1]
    k = 1
    print(solution.topKFrequent(nums, k)) # [1]

    # Example 3:

    nums = [1,2,1,2,1,2,3,1,3,2]
    k = 2
    print(solution.topKFrequent(nums, k)) # [1, 2]