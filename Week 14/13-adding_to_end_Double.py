class Node():
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class DoubleList():
    def __init__(self):
        self.head = None
    def PrintList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" --> ")
                n = n.nref
    def add_to_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            new_node.pref = n.nref
            n.nref = new_node

L1 = DoubleList()
L1.add_to_end(10)
L1.add_to_end(20)
L1.PrintList()