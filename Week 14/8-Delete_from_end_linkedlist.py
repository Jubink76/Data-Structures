class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" --> ")
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

    def delete_end(self):
        if self.head is None:
            print("cant delete the linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            # now we want to go to the 2nd last node
            # and want to make the change reference to None
            n = self.head
            while n.ref.ref is not None:
                n = n.ref  
            n.ref = None

L1 = LinkedList()
L1.add_end(10)
L1.delete_end()
L1.printList()