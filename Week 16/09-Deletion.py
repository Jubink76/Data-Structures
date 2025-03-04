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


    def delete(self,data):
        # check wheather the tree is empty or not 
        if self.key is None:
            print("Tree is empty")
            return
        # check is the data is left or right 
        # applying condition if given  value is less than the root
        if data < self.key:
            # if less than check the left child is available
            if self.left:
                # if avaialble find thee the exact positon of the data by using recursion
                self.left = self.left.delete(data)
            else:
                print("Given node is not present in the tree")
        elif data > self.key:
            # if data is greater than checking the right child
            if self.right:
                # if right is availble finding the exact position
                self.right = self.right.delete(data)
            else:
                print("Given node is not present in the tree")
        else:
            if self.left is None:
                temp = self
                self = None
                return temp
            if self.right is None:
                temp = self
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key)
        return self
    # def delete(self,data):
    #     if self.key is None:
    #         print("BST is empty")
    #         return
    #     if data < self.key:
    #         if self.left:
    #             self.left = self.left.delete(data)
    #         else:
    #             print("node is not found")
    #     elif data > self.key:
    #         if self.right:
    #             self.right = self.right.delete(data)
    #         else:
    #             print("Node is not present")
    #     else:
    #         if self.left is None and self.right is None:
    #             return None
    #         if self.left is None:
    #             return self.right
    #         if self.right is None:
    #             return self.left
    #         node = self.right
    #         while node.left:
    #             node = node.left

    #         self.key = node.key
    #         self.right = self.right.delete(node.key)
    #     return self

root = BST(10)
list1 = [6,3,1,6,98,7]
for i in list1:
    root.insert(i)
root.delete(98)
print("preorder")
root.pre_order()
print()