from solution import Solution, TreeNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1:

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    print(f"Example 1:\n- Input: preorder = {preorder}, inorder = {inorder}\n- Output: {solution.buildTree(preorder, inorder)}\n")


    # Example 2:

    preorder = [-1]
    inorder = [-1]

    print(f"Example 2:\n- Input: preorder = {preorder}, inorder = {inorder}\n- Output: {solution.buildTree(preorder, inorder)}\n")