from solution import Solution, TreeNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    print(f"Example 1: {solution.isSameTree(p, q)}")


    # Example 2:

    p = TreeNode(1)
    p.left = TreeNode(2)

    q = TreeNode(1)
    q.right = TreeNode(2)

    print(f"Example 2: {solution.isSameTree(p, q)}")


    # Example 3:

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)

    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)

    print(f"Example 3: {solution.isSameTree(p, q)}")