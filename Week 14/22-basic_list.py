class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("list is empty")
            return 
        curr = self.head
        while curr:
            print(curr.data,end="-->")
            curr = curr.ref
    
    def insert_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.ref:
            curr = curr.ref
        curr.ref = new_node
    
    def insert_before(self,data,x):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref =self.head
            self.head = new_node
            return
        curr = self.head
        while curr.ref is not None:
            if curr.ref.data == x:
                break
            curr = curr.ref
        if curr.ref is None:
            print("given node is not present")
            return 
        new_node = Node(data)
        new_node.ref = curr.ref
        curr.ref = new_node
        
    def insert_after(self,data,x):
        if self.head is None:
            print("list is empty")
            return 
        curr = self.head
        while curr is not None:
            if curr.data == x:
                break
            curr = curr.ref
        if curr is None:
            print("value is not found")
            return
        new_node = Node(data)
        new_node.ref = curr.ref
        curr.ref = new_node
    
    def delete(self,x):
        if self.head is None:
            print('list is empty')
            return 
        if self.head.data == x:
            self.head = self.head.ref
            return
        curr = self.head
        while curr.ref is not None:
            if curr.ref.data == x:
                break
            curr = curr.ref
        if curr.ref is None:
            print("value is not found")
            return 
        curr.ref = curr.ref.ref
    
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
            return 
        if self.head.ref is None:
            self.head = None
            print("list is emtpy now")
            return
        self.head = self.head.ref
    
    def delete_from_last(self):
        if self.head is None:
            print("Linked list is empty")
            return 
        if self.head.ref is None:
            self.head = None
            print("list is emtpy now")
            return
        curr = self.head
        while curr.ref.ref is not None:
            curr = curr.ref
        curr.ref = None
    
    def search_node(self,x):
        if self.head is None:
            print("empty list")
            return
        index = 0
        curr = self.head
        while curr is not None:
            if curr.data == x:
                print(f"data found at index {index}")
                return
            curr = curr.ref
            index += 1
        print("node is not found")
    
    def list_length(self):
        if self.head is None:
            return 0
        lenght = 1
        curr = self.head
        while curr.ref is not None:
            curr = curr.ref
            lenght += 1
        return lenght
    
    def rev_list(self):
        if self.list_length() >  1:
            pre = None
            curr = self.head
            while curr:
                next_node = curr.ref
                curr.ref = pre
                pre = curr
                curr = next_node
            self.head = pre
            
    def find_mid(self):
        if self.head is None:
            print("list is emtpy")
            return
        slow = self.head
        fast = self.head
        while fast and fast.ref:
            slow = slow.ref
            fast = fast.ref.ref
        
        return slow.data
            
    def freq_count(self,x):
        if self.head is None:
            print("list is empty")
            return
        count = 0
        curr = self.head
        while curr:
            if curr.data == x:
                count += 1
            curr = curr.ref
        return count
        
    def is_palindrom(self):
        if self.head is None or self.head.ref is None:
            return True
    
        slow = fast = self.head
        pre_slow = None
        while fast and fast.ref:
            pre_slow = slow
            slow = slow.ref
            fast = fast.ref.ref
    
        def reverse(node):
            pre = None
            curr = node
            while curr:
                next_node = curr.ref
                curr.ref = pre
                pre = curr
                curr = next_node
            return pre
        second_half_head = reverse(slow)
        first_half = self.head
        second_half =second_half_head
        result = True
        while second_half:
            if first_half.data != second_half.data:
                result = False
                break
            first_half = first_half.ref
            second_half = second_half.ref
        
        restored = reverse(second_half_head)
        if pre_slow:
            pre_slow.ref = restored
        else:
            self.head.ref = restored
        return result
        
        

        
        
L1 = LinkedList()
L1.insert_begin(10)
L1.insert_end(50)
L1.insert_end(60)
L1.insert_before(40,50)
L1.insert_before(5,10)
L1.insert_after(7,5)
L1.insert_after(100,60)
L1.search_node(50)
print(L1.list_length())
L1.rev_list()
print(L1.find_mid())
print(L1.freq_count(10))
print(L1.is_palindrom())
L1.display()
        
        