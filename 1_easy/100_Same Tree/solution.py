from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Solution 1 (NeetCode)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # first check if both trees are None
            return True
        if not p or not q or p.val != q.val: # second check if either tree is None, or values p and q are not equal
            return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


    # Solution 2 (Greg Hogg)
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def balanced(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return balanced(p.left, q.left) and balanced(p.right, q.right)
        
        return balanced(p, q)