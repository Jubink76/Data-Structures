import heapq
# heap = []
# heapq.heappush(heap,5)
# heapq.heappush(heap,2)
# heapq.heappush(heap, 8)
# heapq.heappush(heap, 1)

# print(heap)
# print(heapq.heappop(heap))
# print(heap)

# heapq.heappushpop(heap,3)
# print(heap)

list1 = [9,5,7,3,2]
heapq.heapify(list1)
print(list1) # by default min-heap

print(heapq.nlargest(2,list1))
print(heapq.nsmallest(2,list1))