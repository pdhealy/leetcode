from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Solution 1 (NeetCode)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True # An empty tree is a subtree of any tree
        if not root: return False # If root is empty but subRoot is not, then subRoot cannot be a subtree of root

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        
    def sameTree(self, root, subRoot):
        if not root and not subRoot: # check if both trees are empty indicating end of a branch
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    (self.sameTree(root.right, subRoot.right)))
        return False
        

    # Solution 1 (Greg Hogg)
    def isSubtree2(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return sameTree(p.left, q.left) and sameTree (p.right, q.right)
        
        def has_subtree(root):
            if not root:
                return False
            
            if sameTree(root, subRoot):
                return True
            
            return has_subtree(root.left) or has_subtree(root.right)
        
        return has_subtree(root)
        # Time: O(m * n)
        # Space: O(n)