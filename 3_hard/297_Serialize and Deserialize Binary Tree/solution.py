from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # Solution 1 (NeetCode)
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",") # converts comma-seperated string to list
        self.i = 0 # mutable index to keep track of current position in list across recursive calls. Used instead of local variable

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

    # Solution 2 (Copilot)
    def serialize2(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if not node:
                return 'None,'
            return str(node.val) + ',' + helper(node.left) + helper(node.right)
        return helper(root)

    def deserialize2(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(data_list):
            if data_list[0] == 'None':
                data_list.pop(0)
                return None
            node = TreeNode(int(data_list[0]))
            data_list.pop(0)
            node.left = helper(data_list)
            node.right = helper(data_list)
            return node
        data_list = data.split(',')
        return helper(data_list)