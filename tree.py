from BinaryNode import BinaryNode

tree: BinaryNode = BinaryNode(20)
tree.right = BinaryNode(100)
tree.right.left = BinaryNode(29)
tree.right.left.left = BinaryNode(50)
tree.right.right = BinaryNode(100)
tree.left = BinaryNode(29)
tree.left.right = BinaryNode(60)
tree.left.right.right = BinaryNode(67)
tree.left.left = BinaryNode(23)

