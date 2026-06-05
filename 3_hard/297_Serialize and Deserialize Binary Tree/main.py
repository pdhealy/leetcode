from collections import deque
from solution import Codec, TreeNode


def tree_to_list(root):
    if not root:
        return "[]"

    values = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            values.append("null")
            continue

        values.append(str(node.val))
        queue.append(node.left)
        queue.append(node.right)

    while values and values[-1] == "null":
        values.pop()

    return f"[{','.join(values)}]"

if __name__ == "__main__":

    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()

    # Example 1:
    # input: root = [1,2,3,null,null,4,5]
    # output: [1,2,3,null,null,4,5]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    ans = deser.deserialize(ser.serialize(root))
    print(f"Example 1 (Serialize): {tree_to_list(root)}")
    print(f"Example 1 (Deserialize): {tree_to_list(ans)}")

    # Example 2:
    # input: root = []
    # output: []

    root = None
    ans = deser.deserialize(ser.serialize(root))
    print(f"Example 2 (Serialize): {tree_to_list(root)}")
    print(f"Example 2 (Deserialize): {tree_to_list(ans)}")