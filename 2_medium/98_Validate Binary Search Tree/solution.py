from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid(node, left, right):
            if not node:
                return True # an empty tree is a valid BST
            
            if node.val <= left or node.val >= right:
                return False
            
            return (is_valid(node.left, left, node.val) and 
                    is_valid(node.right, node.val, right))

        return is_valid(root, float('-inf'), float('inf')) # left and right bounds are set to negative and positive infinity, because no limits on the values of the nodes in the BST.