class Node:
    def __init__(self,key):
        self.left= None
        self.right = None
        self.val = key

# Preorder Traversal( root  --> left --> right)
def preorder(root):
    if root:
        print(root.val, end= " ")
        preorder(root.left)
        preorder(root.right)
# In order Traversal (left --> root --> Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
# Postorder Traversal (Left --> Right --> Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left =Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
print("preorder Traveresal:")
preorder(root)

print("\ninorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
postorder(root)