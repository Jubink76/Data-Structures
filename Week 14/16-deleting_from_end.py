class Node():
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class DoubleList():
    def __init__(self):
        self.head  = None
    
    def PrintList(self):
        if self.head is None:
            print("list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" --> ")
                n=n.nref
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node

    def delete_end(self):
        if self.head is None:
            print("Nothing to delete the list is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("List is empty after deletion")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

L1 = DoubleList()
L1.add_begin(10)
L1.add_begin(20)
L1.delete_end()
L1.PrintList()
