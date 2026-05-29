from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Solution 1 (Greg Hogg) - slightly cleaner solution
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: # handles edge case where root is None
            return None
        
        queue = collections.deque()
        queue.append(root)
        ans = []

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                # Differs from Solution 1 by not appending None nodes to the queue
                if node.left: queue.append(node.left) # checks if node.left is not None before appending to queue
                if node.right: queue.append(node.right) # checks if node.right is not None before appending to queue

            ans.append(level)

        return ans
        # Time: O(n)
        # Space: O(n)

    # Solution 2 (NeetCode)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # [[1,2], [3,4]]
        res = []

        q = collections.deque() # deque([])
        q.append(root) # entire tree stored in q[0] initially

        while q:
            qLen = len(q) # len(q) always initialized 1 because q[0]
            level = []
            for i in range(qLen):
                node = q.popleft() # Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res