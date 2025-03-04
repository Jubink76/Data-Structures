class HashTable:
    def __init__(self, size= 10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] == value
                return
        self.table[index].append([key,value])
    
    def get(self,key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def remove(self,key):
        index = self.hash_function(key)
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"index{i}: {bucket}")


ht = HashTable()
ht.insert("name","alice")
ht.insert("age",25)
print(ht.get("name"))
ht.remove("age")
ht.display()