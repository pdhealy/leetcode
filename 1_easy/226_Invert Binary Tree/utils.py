class Utils:
    def __init__(self):
        pass

    def print_tree(self, root):
        if not root:
            print([])
            return
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        # Remove trailing None values for a cleaner output
        while result and result[-1] is None:
            result.pop()
        print(result)