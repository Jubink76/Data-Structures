class HashTable:
    def __init__(self,size = 10):
        self.size = size 
        self.table = [None] * size
        self.DELETED = object()
        
    def hash_function(self,key):
        return hash(key)% self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        original_index=  index
        while self.table[index] is not None and self.table[index] is not self.DELETED:
            if self.table[index][0] == key:
                self.table[index][1] = value
                return
            index = (index + 1)% self.size
            if index == original_index:
                raise Exception ("table size is full")
        self.table[index] = (key, value)
    def search(self,key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] is not self.DELETED and self.table[index][0]==key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None
    
    def delete(self,key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] is not self.DELETED and self.table[index][0] == key:
                self.table[index] = self.DELETED
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False
        
    def display(self):
        for i, item in enumerate(self.table):
            if item is self.DELETED:
                print("index",i,"value is DELETED")
            else:
                print("index",i,"value is",item)
            
h = HashTable()
h.insert("name","jubin")
print(h.search("name"))
print(h.delete("name"))
h.display()
        