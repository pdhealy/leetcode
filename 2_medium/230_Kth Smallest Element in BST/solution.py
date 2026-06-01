from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Solution 1 (NeetCode)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # Initialize a counter to keep track of the number of nodes visited.
        stack = [] # Initialize an empty stack to perform an iterative in-order traversal of the binary search tree.
        cur = root

        # TODO: Raise ticket with VSCode regarding debug issue with while loop and stack. The loop is not working as expected when debugging, but it works fine when running the code without debugging.
        while cur or stack: # if cur or stack is empty then exit the loop
            while cur: # if cur is not empty then add it to the stack and move to the left child
                stack.append(cur)
                cur = cur.left

            cur = stack.pop() # If cur is empty it means we have reached the leftmost node, pop the last node from the stack and set it as the current node.
            n += 1 # Increment the count of nodes visited.
            if n == k:
                return cur.val
            cur = cur.right


    # Solution 2 (Greg Hogg)
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        ans = [0]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if count[0] == 1:
                ans[0] = node.val

            count[0] = count[0] - 1
            if count[0] > 0:
                dfs(node.right)

        dfs(root)
        return ans[0]
        # Time: O(n)
        # Space: O(n)