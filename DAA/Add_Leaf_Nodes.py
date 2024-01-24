class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def search(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self, node, result=[]):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

    def get_leaf_nodes(self, node, result=[]):
        if node is not None:
            if node.left is None and node.right is None:
                result.append(node.value)
            else:
                self.get_leaf_nodes(node.left, result)
                self.get_leaf_nodes(node.right, result)
        return result

# Example usage:
bst = BinarySearchTree()
values = input("Enter values to insert into the binary search tree (space-separated): ").split()
for value in values:
    bst.insert(int(value))

leaf_nodes = bst.get_leaf_nodes(bst.root)
print("Leaf nodes of the binary search tree:", leaf_nodes)
