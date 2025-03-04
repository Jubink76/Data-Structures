class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None

class Queue():
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.ref = new_node
        self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        dequeued_data = self.front.data
        self.front = self.front.ref
        if self.front is None:
            self.rear = None
        return dequeued_data
    
    def peak(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data
    
    def is_empty(self):
        return self.front is None