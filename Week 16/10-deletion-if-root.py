class BST():
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            print("Duplicate value is not storing")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    
    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not in the tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")
    
    # when deleting the root node we need to check whether the root node is leaf node
    # that means it contain only just 1 node
    # that time just print a 
    def deletion(self,data):
        if self.key is None:
            print("The tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.deletion(data)
            else:
                print("Given node is not present")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.deletion(data)
            else:
                print("Given data is not present")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            elif self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            else:
                node = self.rchild
                while node.lchild:
                    node = node.lchild
                self.key = node.key
                self.rchild = self.rchild.deletion(node.key)
        return self

    def pre_order(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
 # if the tree has only one node(root node) the deletion operation wont work
 # so first we have to count the nodes
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)

root = BST(10)
list1 = [6,3,1,6,98,7]
for i in list1:
    root.insert(i)
print(count(root))
# root.deletion(10)
root.pre_order()