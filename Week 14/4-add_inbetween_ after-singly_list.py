class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                n = n.ref
            n.ref = new_node

    # creating the new funciton to add after the element,
    # giving of the new node and the data of the position which we want to add after as X
    # we need to  find x first
    def add_after(self,data,x):
        # first node as n
        n = self.head
        # traverse throught the linkedlist for identifying where the x is available
        while n is not None:
            # traverse until the last node reference become zero
            # if it is available before break out from the position, because we are adding after the position

            if x == n.data:
                break
            # updating  the n for next node
            n = n.ref
        if n is None:
            print("node is not present")
        else:
            # if the positon confirmed creating new node
            new_node = Node(data)
            #  assigning new node reference to the reference of the current node, because that is pointing the next node
            new_node.ref= n.ref
            # assigning current node reference to the new node reference, that should point to the new node(next)
            n.ref = new_node

L1 = LinkedList()
L1.add_end(10)
L1.add_after(100,10)
L1.add_after(500,100)
L1.add_after(100000,100)
L1.printList()