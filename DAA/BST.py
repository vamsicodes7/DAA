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

bst = BinarySearchTree()
values = input("Enter values to insert into the binary search tree (space-separated): ").split()
for value in values:
    bst.insert(int(value))

search_value = int(input("Enter a value to search in the binary search tree: "))
if bst.search(search_value):
    print(f"{search_value} is found in the binary search tree.")
else:
    print(f"{search_value} is not found in the binary search tree.")

sorted_elements = bst.inorder_traversal(bst.root)
print("Sorted elements of the binary search tree:", sorted_elements)
