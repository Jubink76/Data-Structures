class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self,index):
        return(index-1)//2 if index > 0 else None
    
    def left_child(self,index):
        return 2 * index + 1
    
    def right_child(self,index):
        return 2 * index + 2
    
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,index):
        parent = self.parent(index)
        while parent is not None and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        # get the minimum element
        root_value = self.heap[0]
        # move lasst element to the root
        self.heap[0] = self.heap.pop()
        # restore heap property
        self.heapify_down(0)
        return root_value
    
    def heapify_down(self,index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest],self.heap[index]
            self.heapify_down(smallest)

    def delete(self,value):
        try:
            index = self.heap.index(value)
            self.heap[index] = self.heap.pop()
            self.heapify_down(index)
        except ValueError:
            print("value not found in the heap")

    def heapify(self,list1):
        self.heap = list1[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify_down(i)


    def heap_sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.extract_min())
        return sorted_list
    
    def display(self):
        print(self.heap)


heap = BinaryHeap()
nums = [10,1,5,20,3]

heap.heapify(nums)
print("Heapified array:",heap.heap)

heap.insert(2)
heap.insert(8)
heap.display()

print("Extracted min:",heap.extract_min())
heap.display()

heap.delete(5)
heap.display()


sorted_array  = heap.heap_sort()
print("Sorted array:",sorted_array)