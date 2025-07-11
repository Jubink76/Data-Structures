class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.DELETED = object()  # Sentinel for deleted entries

    def hash_function(self, key):
        return sum(ord(c) for c in str(key)) % self.size

    def second_hash(self, key):
        # Secondary hash must be non-zero and ideally relatively prime to table size
        return 1 + (sum(ord(c) for c in str(key)) % (self.size - 1))

    def insert(self, key, value):
        index1 = self.hash_function(key)
        index2 = self.second_hash(key)
        i = 0

        while i < self.size:
            index = (index1 + i * index2) % self.size
            if self.table[index] is None or self.table[index] is self.DELETED:
                self.table[index] = (key, value)
                return True
            if self.table[index][0] == key:
                self.table[index] = (key, value)  # Update value
                return True
            i += 1

        print("Table is full")
        return False

    def search(self, key):
        index1 = self.hash_function(key)
        index2 = self.second_hash(key)
        i = 0

        while i < self.size:
            index = (index1 + i * index2) % self.size
            if self.table[index] is None:
                return None
            if self.table[index] is not self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
            i += 1

        return None

    def delete(self, key):
        index1 = self.hash_function(key)
        index2 = self.second_hash(key)
        i = 0

        while i < self.size:
            index = (index1 + i * index2) % self.size
            if self.table[index] is None:
                return False
            if self.table[index] is not self.DELETED and self.table[index][0] == key:
                self.table[index] = self.DELETED
                return True
            i += 1

        return False

ht = DoubleHashingHashTable(7)

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("grape", 30)

print(ht.search("banana"))   # ➜ 20
print(ht.search("grape"))    # ➜ 30

ht.delete("banana")
print(ht.search("banana"))   # ➜ None

ht.insert("banana", 25)
print(ht.search("banana"))   # ➜ 25
