class Node():
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BST():
    def __init__(self):
        self.root = None
    def insert(self,key):
        if self.root is None:
            self.root = Node(key) 
        else:
            self.insert_recursive(self.root,key)
    def insert_recursive(self,node,key):
        if key == node.key:
            print("Duplicate values are not allowed")
            return
        elif key < node.key:
            if node.left:
                self.insert_recursive(node.left,key)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self.insert_recursive(node.right,key)
            else:
                node.right = Node(key)

    def pre_order(self,node):
        if node:
            print(node.key,end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)
    


bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(4)
bst.insert(5)
bst.insert(7)
bst.insert(87)
bst.insert(25)

print(bst.pre_order(bst.root))