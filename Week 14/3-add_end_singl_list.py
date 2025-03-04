# creating node for linked list implementation
class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None
# connection or creatign the thee linkedlist

class LinkedList():
    def __init__(self):
        self.head = None
    def PrintList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    # after creating the linked list connection we want to create a new node for adding to the end

    def add_end(self,data):
        new_node = Node(data)
        # we want to move the last node of the current linked list
        # before that we need to check the current linked list is empty or not
        if self.head is None:
            self.head = new_node
        else:
            # if there is existing elements, we want to tranvese to the last element
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

l1 = LinkedList()
l1.add_end(10)
l1.add_end(50)
l1.add_end(100)
l1.PrintList()