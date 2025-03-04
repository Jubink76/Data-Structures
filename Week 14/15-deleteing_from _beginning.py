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
            print("Double linked is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end = " --> ")
                n = n.nref
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("Nothing to delete, list is emepty")
            return
        if self.head.nref is None:
            self.head = None
            print("Double list is empty now")
        else:
            self.head = self.head.nref
            self.head.pref = None


L1 = DoubleList()
L1.add_begin(10)
L1.add_begin(20)
L1.delete_begin()
L1.PrintList()