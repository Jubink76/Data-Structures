class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        if self.head is None:
            print("linked list  is empty")
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
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_before(self,data,x):
            # At first we want to check the linked list is empty or not other wise it will raise error for None.data
            if self.head is None:
                print("Linked List is empty")
                return
            # first we need to check wheather the data is adding before the first node(current head)
            # this is the case of if we adding the element before the first node
            if self.head.data == x:
                new_node = Node(data)
                new_node.ref = self.head
                self.head = new_node
                return
            # but if we adding the node in between any other position before any second or third.....
            # we need to bother about the address reference of the rest
            # for that first identify the previous  node
            # Then new node aftere the previous node
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node is not found")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

L1 = LinkedList()
L1.add_end(100)
L1.add_end(500)
L1.add_before(200,500)
L1.add_before(10,100)
L1.printList()