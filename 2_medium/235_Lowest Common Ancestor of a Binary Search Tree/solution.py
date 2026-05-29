# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Solution 1 (NeetCode)
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': # 'TreeNode' is a forward reference. Function is expected to always return a TreeNode, never None. Optional[TreeNode] only needed if None is possible return value
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val: # BST structures are defined by node values, not node positions: left children are less than the parent, right children are greater.
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


    # Solution 2 (Greg Hogg)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]

        def search(root):
            if not root:
                return
            
            lca[0] = root
            if root is p and root is q: # check if root is both p and q meaning they are same node
                return
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                return
        
        search(root)
        return lca[0]
    
    # Time: O(h)
    # Space: O(h)