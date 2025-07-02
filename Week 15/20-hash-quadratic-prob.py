class HashTable:
    def __init__(self,size = 10):
        self.size = size
        self.table = [None] * size
        self.DELETED = object()
    
    def hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        original_index = index
        i = 1
        while self.table[index] is not None and self.table[index] is not self.DELETED:
            if self.table[index][0] == key:
                self.table[index][1] = value
                return True
            index = (original_index + i*i) % self.size
            i += 1
            if i == self.size:
                print("table is fulled")
                return False
        self.table[index] = (key,value)
        return True
        
    def delete(self,key):
        index = self.hash_function(key)
        original_index = index
        i = 1
        while self.table[index] is not None and self.table[index] is not self.DELETED:
            if self.table[index][0] == key:
                self.table[index] = self.DELETED
                return True
            index = (original_index + i* i) % self.size
            i = i +1
            if i == original_index:
                break
        return False
    
    def display(self):
        for i , item in enumerate(self.table):
            if item is self.DELETED:
                print("index",i,"value is DELETED")
            else:
                print("index",i,"value is ",item)
                

h = HashTable()
h.insert("name","jubin")
h.insert("a","apple")
h.insert("b","ball")
h.delete("b")
h.display()