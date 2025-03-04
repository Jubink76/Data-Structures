# first we need to create a node
# compared to single linkedList there are 2 references
class Node():
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

# creating the Double linked list as similar to the sinlgy list
class DoubleList():
    def __init__(self):
        self.head = None
    def PrintDouble(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head 
            while n is not None:
                print(n.data, end=" --> ")
                n = n.nref
    def ReverseList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.ref is not None:
                n = n.nref
            while n is not None:
                print(n.data,end = " --> ")
                n = n.pref

L1 = DoubleList()
L1.PrintDouble()
L1.ReverseList()