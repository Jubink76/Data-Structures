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
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def add_after(self,data,x):
        if self.head is None:
            print("Linked list is empty,cant add")
            return
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print("The given node is not available in the list")
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("The linked list is emtpy")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
        if n is None:
            print("Given node is not found in the list")
        else:
            new_node = Node(data)
            new_node.nref = n
            new_node.pref = n.pref
            if n.pref is not None:
                n.pref.nref = new_node
            else:
                self.head = new_node
            n.pref = new_node



L1 = DoubleList()
L1.add_begin(100)
L1.add_after(1000,100)
L1.PrintList()