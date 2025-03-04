#creting node
class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None
# creting linked list and traversing
class LinkedList():
    def __init__(self):
        self.head = None
    def PrintList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" --> ")
                n = n.ref
# function to add data to  the linkedlist
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
# function to delete the data to the linked list 

    def delete_by_value(self,x):
        # checking the linked list is empty for deleting the data
        if self.head is None:
            print("cant delete,Linked List is empty")
            return
        #also checking if the value is first node of the linkedlist
        if x == self.head.data:
            self.head= self.head.ref
            return
        # or else the value is lies somewhere in the linked list
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Linked list not containing the x value")
        else:
            n.ref = n.ref.ref


L1 = LinkedList()
L1.add_begin(10)
L1.add_begin(100)
L1.add_begin(200)
L1.delete_by_value(10)
L1.PrintList()