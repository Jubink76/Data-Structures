# using class
class Stack():
    def __init__(self):
        self.stack = []
    # for empty stack
    def is_empty(self):
        return len(self.stack) == 0
    # for adding element in the stack
    def push(self,item):
        self.stack.append(item)
    # for removing element fromm the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    # for top element in the stack
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
s = Stack()
s.push(10)
s.push(20)
print(s.pop())
print(s.pop())
print(s.pop())


stack = []
stack.append(10)
stack.append(20)
print(stack)
stack.pop()
stack.pop()