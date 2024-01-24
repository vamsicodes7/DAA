class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def print_spiral(self):
        if not self.root:
            return

        left_to_right = True
        current_level = [self.root]

        while current_level:
            next_level = []
            for node in current_level:
                print(node.value, end=" ")

                if left_to_right:
                    if node.left:
                        next_level.insert(0, node.left)
                    if node.right:
                        next_level.insert(0, node.right)
                else:
                    if node.right:
                        next_level.insert(0, node.right)
                    if node.left:
                        next_level.insert(0, node.left)

            left_to_right = not left_to_right
            current_level = next_level

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    elements = [1, 3, 2, 4, 5, 6, 7, 15, 13, 12, 11, 10, 9, 8]
    for element in elements:
        tree.insert(element)

    print("Spiral Order Traversal:")
    tree.print_spiral()
