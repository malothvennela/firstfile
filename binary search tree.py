class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return Node(value)
    elif value > root.value:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,end=" ")
        inorder(root.right)
root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,10)
root = insert(root,1)
root = insert(root,6)
print("inorder traversal:")
inorder(root)

