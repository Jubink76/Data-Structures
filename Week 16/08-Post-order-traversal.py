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
            print("Duplicate is not allowd")
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
    
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.key,end= " ")

bst = BST(None)
list1 = [10,5,3,8,15,12]
for i in list1:
    bst.insert(i)

bst.post_order()