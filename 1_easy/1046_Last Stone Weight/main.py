from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    stones = [2,7,4,1,8,1]
    ans = solution.lastStoneWeight(stones)
    print(f"Example 1: {ans}")  # 1

    # Example 2:

    stones = [1]
    ans = solution.lastStoneWeight(stones)
    print(f"Example 2: {ans}")  # 1