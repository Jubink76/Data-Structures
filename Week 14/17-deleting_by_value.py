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

    def delete_by_value(self,x):
        if self.head is None:
            print("Nothing to delete list is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("Linked list is empty after deletion")
            return
        if self.head.data == x:
            self.head.nref = self.head
            self.head.pref = None
        else:
            n = self.head
            while n.nref is not None:
                if n.data == x:
                    break
                n = n.nref
            if n.nref is not None:
                n.nref.pref = n.pref
                n.pref.nref = n.nref
            else:
                if n.data == x:
                    n.pref.nref = None
                else:
                    print("The value not lies in this list")
            

L1 = DoubleList()
L1.add_begin(10)
L1.add_begin(20)
L1.add_begin(30)
L1.delete_by_value(20)
L1.PrintList()