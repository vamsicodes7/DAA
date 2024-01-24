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

def search_node(root, value):
    if root is None or root.value == value:
        return root is not None

    if root.value < value:
        return search_node(root.right, value)

    return search_node(root.left, value)

# Creating the BST with the provided nodes: 10, 8, 20, 9, 7, 21, 15
root = None
nodes = [10, 8, 20, 9, 7, 21, 15]
for node in nodes:
    root = insert_node(root, node)

# Taking user input for the node to search
user_input = int(input("Enter the value to search: "))

# Searching for the user input node
result = search_node(root, user_input)

# Printing the result
print(result)
