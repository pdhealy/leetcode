from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None): # each node (e.g., root.left.left) is an object with its own left and right properties
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # check if root is None
            return None

        # swap the children nodes
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # seperate function calls for left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root