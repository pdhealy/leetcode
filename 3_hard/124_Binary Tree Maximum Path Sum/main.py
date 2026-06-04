from solution import Solution, TreeNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(f"Example 1: {solution.maxPathSum(root)}")


    # Example 2:

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(f"Example 2: {solution.maxPathSum(root)}")