class Node():
    def __init__(self,data):
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
                print(n.data,end="")
                n = n.ref
    def add_to_empty(self,data):
        if self.head is None:
            new_node =Node(data)
            self.head = new_node
        else:
            print("LinkedList is not empty")


L1 = LinkedList()
L1.add_to_empty(10)
L1.add_to_empty(500)
L1.printList()