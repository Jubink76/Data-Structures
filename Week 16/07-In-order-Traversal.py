class BST():
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            print("Not storing duplicate")
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
                print("NOde is not found")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node is not found")

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.key,end=" ")
        if self.right:
            self.right.in_order()
    

bst = BST(None)
list1 = [10,5,3,8,15,12]
for i in list1:
    bst.insert(i)
bst.in_order()