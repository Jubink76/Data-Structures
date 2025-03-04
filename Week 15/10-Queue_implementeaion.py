class Queue():
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return len(self.queue) == 0
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return "Queue is empty"
    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        return "Queue is empty"
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())
print(q.front())
