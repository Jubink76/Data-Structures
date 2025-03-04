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
            print("Duplicates are not storing")
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
            print("Data is found")
            return
        if data < self.key:
            if self.left:
                self.left.search(data)
            else:
                print("Data is not found in the BST")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Data is not found")
    
    def pre_order(self):
        print(self.key,end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()


bst = BST(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(12)
bst.pre_order()