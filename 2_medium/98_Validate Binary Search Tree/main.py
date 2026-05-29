from solution import Solution, TreeNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(f"Example 1: {solution.isValidBST(root)}")


    # Example 2:

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(f"Example 2: {solution.isValidBST(root)}")