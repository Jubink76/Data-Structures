class BST():
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def pre_order(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def find_min(self):
        if self.key is None:
            print("Tree is empty")
            return
        current = self
        while current.lchild:
            current = current.lchild
        print("Smallest elemtnt:", current.key)

    def find_max(self):
        if self.key is None:
            print("Tree is empty")
            return
        current = self
        while current.rchild:
            current = current.rchild
        print("maximum element is :",current.key)

    
root = BST(10)
list1 = [21,2,4,7,19,20,40,9]
for i in list1:
    root.insert(i)
root.pre_order()
root.find_max()
root.find_min()