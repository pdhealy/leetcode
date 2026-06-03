from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) # the first element in preorder is the root
        mid = inorder.index(preorder[0]) # find the index of the root in inorder to split left and right subtrees
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) # recursively build the left subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) # recursively build the right subtree
        # return the binary tree node
        return root