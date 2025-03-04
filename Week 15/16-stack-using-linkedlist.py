class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None
    
    def push(self,data):
        new_node = Node(data)
        new_node.ref = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stck is empty")
            return None
        return self.top.data
    def peak(self):
        if self.isEmpty():
            print("stck is empty")
            return None
        return self.top.data
    def display(self):
        if self.isEmpty():
            print("stack is empty")
            return 
        current = self.top
        while current:
            print(current.data, end=" --> ")
            current = current.ref
        print("none")


stack = Stack()
stack.push(10)
stack.push(20)

stack.display()