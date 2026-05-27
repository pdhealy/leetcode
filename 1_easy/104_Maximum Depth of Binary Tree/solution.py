from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Solution 1 (NeetCode) - using iteration
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res


    # Solution 2 (Greg Hogg) - using recursion
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
    
        # Time: O(n)
        # Space: O(n)


    # Solution 3 (Greg Hogg) - using recursion, with layer tracking for debugging
    def maxDepth3(self, root: Optional[TreeNode], layer: int = 1) -> int:
        # Print the current layer for debugging/tracking (custom)
        print(f"Recursion layer: {layer}, Node value: {getattr(root, 'val', None)}")

        if not root:
            return 0

        left = self.maxDepth3(root.left, layer + 1)
        right = self.maxDepth3(root.right, layer + 1)

        return 1 + max(left, right)

        # Time: O(n)
        # Space: O(n)