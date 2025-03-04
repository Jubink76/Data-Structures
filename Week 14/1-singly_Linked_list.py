### Traversal throught linked list 


# To create a singly linked list first we have to create a node
# IMPLEMENTAION OF SINGLY LINKED LIST

class Node():
    # Each node contain data and reference
    def __init__(self,data):
        self.data = data
        self.ref = None

# now we can create the individual node by using this class
# linked list is the connection of nodes . or chain of nodes
# Afte creating each node we need to connect that
# for connecting we need to create another class 

class LinkedList():
    def __init__(self):
        # other than the node what is present in the linked list , that is head
        # head is the starting point of the linkedlist contain the link of reference of the first node
        # initialize the head 
        self.head = None # it means empty linked list
    # for traverse on the linked list we want to check each elements in the linked list
    def printList(self):
        # check the head is none the linked list is empty
        if self.head is None:
            print("linked list is empty")
        else:
            # we dont know the actual size of the linked list but we know the condition where to stop, so use while loop
            # assigning the head into new variable
            n = self.head
            while n is not None:
                # iterating until the reference is null
                # printing the data of each node
                print(n.data)
                # updating the iterator to next node
                n = n.ref

                
L1 = LinkedList()
L1.printList()



### Adding a new node in the beginning of the linkedlist

