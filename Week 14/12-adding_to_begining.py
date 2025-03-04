class Node():
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class DoubleList():
    def __init__(self):
        self.head = None
    def printList(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end= " --> ")
                n = n.nref
    def add_to_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node
L1 = DoubleList()
L1.add_to_begin(10)
L1.add_to_begin(20)
L1.printList()