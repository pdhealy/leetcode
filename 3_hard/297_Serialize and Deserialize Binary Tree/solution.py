from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if not node:
                return 'None,'
            return str(node.val) + ',' + helper(node.left) + helper(node.right)
        return helper(root)


    def deserialize(self, data: str) -> Optional[TreeNode]:
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