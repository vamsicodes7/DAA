class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return Node(value)
    else:
        if root.value < value:
            root.right = insert_node(root.right, value)
        else:
            root.left = insert_node(root.left, value)
    return root

def find_leaf_nodes(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.value]
    left_leaves = find_leaf_nodes(root.left)
    right_leaves = find_leaf_nodes(root.right)
    return left_leaves + right_leaves

def sum_leaf_nodes(root):
    leaf_nodes = find_leaf_nodes(root)
    return sum(leaf_nodes)

# Creating the BST with the provided nodes: 10, 8, 20, 9, 7, 21, 15
root = None
nodes = [10, 8, 20, 9, 7, 21, 15]
for node in nodes:
    root = insert_node(root, node)

# Finding and printing the sum of leaf nodes
leaf_sum = sum_leaf_nodes(root)
print("Sum of leaf nodes in the BST:", leaf_sum)
