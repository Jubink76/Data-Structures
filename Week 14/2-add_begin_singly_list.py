# ADDING THE ELEMENT IN THE BEGINNING OF THE LINKED LIST

# for adding the elemnt in the begining first we are doing the creation of linked list which we done before

# creating node
class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None
# connecting the node (creating linkedlist)
class LinkedList():
    def __init__(self):
        self.head = None
    def printlist(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n = n.ref
    # after creating the linked list we want to add the element at the begining
    def add_begin(self,data):
        # for adding new element first we want create new node
        # for creating new node we have a class and creating new object for new not and passign data
        new_node = Node(data)
        # link the reference of the first node to the new node
        new_node.ref = self.head
        self.head = new_node
        # changing the head to the new node

L1 = LinkedList()
L1.add_begin(10)
L1.add_begin(50)
L1.printlist()