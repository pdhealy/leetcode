from solution import Codec, TreeNode

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
    print(ser.serialize(root))
    print(ser.serialize(ans))

    # Example 1:

    root = Codec().deserialize('1,2,None,None,3,4,None,None,5,None,None,')
    assert Codec().serialize(root) == [1,2,3,null,null,4,5]

    # Example 2:

    root = Codec().deserialize('None,')
    assert Codec().serialize(root) == []