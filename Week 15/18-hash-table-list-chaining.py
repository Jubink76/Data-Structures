class HashTable:
    def __init__(self,size=10):
        self.size = size 
        self.table = [[] for _ in range(self.size)]
    
    def hash_function(self,key):
        return hash(key)% self.size
        
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        
    def display(self):
        for pair in self.table:
            print(pair)
            
    def search(self,key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self,key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False
            
h = HashTable()
h.insert("name","jubin")
h.insert('a','apple')
h.insert('b','ball')
h.insert('c','cat')
print(h.search('c'))
print(h.delete('c'))
h.display()