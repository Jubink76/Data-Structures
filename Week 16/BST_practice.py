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
            print("duplicate")
            return
        if data < self.key:
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
        if self.key is None:
            return
        if self.key == data:
            print("found")
            return
        if data < self.key:
            if self.left:
                self.left.search(data)
            else:
                print("value not found")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("value not found")
    
    def delete(self,data):
        if self.key is None:
            return
        if data < self.key:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("value does not exist")
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("value does not exist")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key)
        return self
    
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.key,end=" ")
        if self.right:
            self.right.in_order()
    
    def pre_order(self):
        print(self.key,end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
    
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.key,end=" ")
    
    def find_min(self):
        if self.key is None:
            return
        current = self
        while current.left:
            current = current.left
        print("Smalles value is :",current.key)
    
    def find_max(self):
        if self.key is None:
            return
        current = self
        while current.right:
            current = current.right
        print("Greatest value:",current.key)

    def find_depth(self):
        if self is None:
            return 0
        left_depth = self.left.find_depth() if self.left else 0
        right_depth = self.right.find_depth() if self.right else 0
        return max(left_depth,right_depth) + 1

    def count_node(self):
        if self is None:
            return 0
        left_count = self.left.count_node() if self.left else 0
        right_count = self.right.count_node() if self.right else 0
        return 1 + left_count + right_count
    
    def is_bst(self,min_val=float('-inf'),max_val=float('inf')):
        if self is None:
            return True
        if not (min_val < self.key < max_val):
            return False
        left_Valid = self.left.is_bst(min_val,self.key) if self.left else True
        right_valid = self.right.is_bst(self.key,max_val) if self.right else True

        return left_Valid and right_valid
    
    def kth_small(self,k,counter=[0]):
        if self is None:
            return None
        if self.left:
            left = self.left.kth_small(k,counter)
            if left is not None:
                return left
        counter[0] += 1
        if counter[0] == k:
            return self.key
        if self.right:
            return self.right.kth_small(k,counter)
        return None
    
    def kth_large(self,k,counter=[0]):
        if self.right:
            right = self.right.kth_large(k,counter)
            if right is not None:
                return right
        counter[0] += 1
        if counter[0] == k:
            return self.key
        if self.left:
            return self.left.kth_large(k,counter)
        
    def is_balanced(self):
        def height(self):
            if self is None:
                return 0
            left_height = height(self.left)
            right_height = height(self.right)
            if abs(left_height -right_height) > 1:
                return - 1
            return 1 + max(left_height,right_height)
        return height(self) != -1
    
    def lca(self,n1,n2):
        if self.key is None:
            return None
        if self.key > n1 and self.key > n2:
            return self.left.lca(n1,n2) if self.left else None
        if self.key < n1 and self.key < n2:
            return self.right.lca(n1,n2) if self.right else None
        return self.key
        
list1 = [1,5,2,8,15,25,98,253,37,9,100]
bst = BST(None)
for i in list1:
    bst.insert(i)
bst.delete(25)
print("inorder traversal:")
bst.in_order()
print("\npre order traversal")
bst.pre_order()
print("\npostorder travesal")
bst.post_order()
bst.find_max()
bst.find_min()
print("depth of the tree:",bst.find_depth())
print("Number of nodes in the tree:",bst.count_node())
print(bst.is_bst())
print("kth smallest",bst.kth_small(3))
print("kth largest",bst.kth_large(3))
print("BST is balanced?",bst.is_balanced())
print("lowest common ancestor is:",bst.lca(9,253))