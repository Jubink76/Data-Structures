# Initialization method

class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

root = BST(10)
print(root.key)
print(root.left)
print(root.right)