from BinaryTree import Node, BinaryTree

# test_node = Node(10)
# test_node.left = Node(5)
# test_node.right = Node(15)

# print(test_node, test_node.left, test_node.right)

test_tree = BinaryTree()
test_tree.insert(15)
test_tree.insert(7)
test_tree.insert(3)
test_tree.insert(9)
test_tree.insert(22)
test_tree.insert(28)
print('tree root', test_tree.root)
print('roots left node', test_tree.root.left)
print('roots left left', test_tree.root.left.left)

print('roots lefs lefts right', test_tree.root.left.right)
print('roots right node', test_tree.root.right)
print('roots right right', test_tree.root.right.right)

# test_tree.print()

print('searching for 9', test_tree.search(9))
print('searching for 77', test_tree.search(77))
print('max is', test_tree.get_max())
print('min is', test_tree.get_min())
print('the size of the tree is', test_tree.size())
print('the height of the tree is', test_tree.height())