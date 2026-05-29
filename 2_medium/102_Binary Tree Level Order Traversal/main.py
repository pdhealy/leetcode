from logging import root

from solution import Solution, TreeNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(f"Example 1: {solution.levelOrder(root)}")


    # Example 2:

    root = TreeNode(1)
    print(f"Example 2: {solution.levelOrder(root)}")


    # Example 3:

    root = None
    print(f"Example 3: {solution.levelOrder(root)}")