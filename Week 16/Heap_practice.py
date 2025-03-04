class Heap():
    def __init__(self):
        self.heap = []
    
    def parent(self,index):
        return (index - 1) // 2 if index > 0 else None
    
    def left_child(self,index):
        return 2 * index + 1
    
    def right_child(self,index):
        return 2 * index + 2
    

    def heapify(self,index):
        parent = self.parent(index)
        while parent is not None and self.heap[parent] > self.heap[index]:
            self.heap[parent],self.heap[index] = self.heap[index],self.heap[parent]
            index = parent
            parent = self.parent(index)

    def insert(self,value):
        self.heap.append(value)
        self.heapify(len(self.heap)-1)

    def display(self):
        print(self.heap)

    def heapify_down(self,index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest= left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index] , self.heap[smallest] = self.heap[smallest],self.heap[index]
            self.heapify_down(smallest)
    
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root_value 
    
    def heap_sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.extract_min())
        return sorted_list
    
    def delete(self,value):
        try:
            index = self.heap.index(value)
            last_value = self.heap.pop()
            if index < len(self.heap):
                self.heap[index] = last_value
                parent = self.parent(index)
                if parent is not None and self.heap[index] < self.heap[parent]:
                    self.heapify(index)
                else:
                    self.heapify_down(index)
        except:
            print("value does not exist")

heap = Heap()
heap.insert(10)
heap.insert(20)
heap.insert(320)
heap.insert(4)
heap.display()
heap.delete(20)
heap.display()

import heapq

heap = []
heapq.heappush(heap,10)
heapq.heappush(heap,5)
heapq.heappush(heap,20)
print(heap)