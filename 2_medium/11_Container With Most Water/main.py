# 11. Container With Most Water

from solution import Solution

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    height = [1,8,6,2,5,4,8,3,7]
    # Output: 49
    # Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

    # Example 2:
    # height = [1,1]
    # Output: 1

    output = solution.maxArea(height)
    print(f"Max area of water the container can contain: {output}")