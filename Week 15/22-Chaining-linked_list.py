class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        head = self.table[index]
        
        # Update if key exists
        curr = head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        
        # Insert at head
        new_node = Node(key, value)
        new_node.next = head
        self.table[index] = new_node
    
    def search(self, key):
        index = self.hash_function(key)
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None
    
    def delete(self, key):
        index = self.hash_function(key)
        curr = self.table[index]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[index] = curr.next
                return True
            prev = curr
            curr = curr.next
        return False
