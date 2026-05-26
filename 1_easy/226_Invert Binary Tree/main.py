from solution import Solution
from solution import TreeNode
from utils import Utils

if __name__ == "__main__":
    solution = Solution()
    utils = Utils()

    # Example 1:

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print(f"---------Example 1---------")
    utils.print_tree(solution.invertTree(root))


    # Example 2:

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(f"---------Example 2---------")
    utils.print_tree(solution.invertTree(root))

    # Example 3:

    root = None

    print(f"---------Example 3---------")
    utils.print_tree(solution.invertTree(root))