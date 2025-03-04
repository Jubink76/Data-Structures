class BST():
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            print("Not storing duplicate values")
            return
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
    
    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.left:
                self.left.search(data)
            else:
                print("Node is not present in tree")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node is not present in Tree")


root = BST(10)
list1 = [6,3,1,6,98,3,8]
for i in list1:
    root.insert(i)
root.search(6)