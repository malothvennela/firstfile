def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        if current_node is None:
            return current_node
        if value < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, value)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                min_node = self._find_min(current_node.right)
                current_node.value = min_node.value
                current_node.right = self._delete_recursive(current_node.right, min_node.value)
        return current_node

    def _find_min(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def update(self, old_value, new_value):
        self.delete(old_value)
        self.insert(new_value)

    def inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):
        if current_node:
            self._inorder_recursive(current_node.left)
            print(current_node.value, end=" ")
            self._inorder_recursive(current_node.right)
bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
print("Inorder traversal:")
bst.inorder()
print("\nDeleting 6...")
bst.delete(6)
print("Inorder traversal after deletion:")
bst.inorder()
print("\nUpdating 3 to 4...")
bst.update(3, 4)
print("Inorder traversal after update:")
bst.inorder()
