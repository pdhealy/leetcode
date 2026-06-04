from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution 1 (NeetCode)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]

    # Solution 2 (Copilot)
    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            current_sum = node.val + left_sum + right_sum
            self.max_sum = max(self.max_sum, current_sum)

            return node.val + max(left_sum, right_sum)

        dfs(root)
        return self.max_sum
        