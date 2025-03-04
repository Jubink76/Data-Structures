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

    

root = BST(10)
list1 = [2,6,8,36,12,63,20]
for i in list1:
    root.insert(i)