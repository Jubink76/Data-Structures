class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        if self.head is None:
            print("linked_list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="-->")
                n = n.ref
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def delete_begin(self):
        # for deleting there is no need of parameters
        # first we want check the linked list is none or not
        if self.head is None:
            print("Linked list is empty ,cant delete!")
        else:
            # only move the head to the next node
            self.head = self.head.ref

L1 = LinkedList()
L1.add_end(10)
L1.add_end(20)
L1.add_end(30)
L1.delete_begin()
L1.printList()