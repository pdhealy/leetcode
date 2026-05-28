from solution import Solution, TreeNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    p = TreeNode(2)
    q = TreeNode(8)

    print(f"Example 1: {solution.lowestCommonAncestor(root, p, q).val}")

    # Example 2:
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    p = TreeNode(2)
    q = TreeNode(4)

    print(f"Example 2: {solution.lowestCommonAncestor(root, p, q).val}")

    # Example 3:
    root = TreeNode(2)
    root.left = TreeNode(1)
    p = TreeNode(2)
    q = TreeNode(1)

    print(f"Example 3: {solution.lowestCommonAncestor(root, p, q).val}")