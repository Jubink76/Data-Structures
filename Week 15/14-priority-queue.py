# using list

queue = []
queue.append(10)
queue.append(40)
queue.sort()
queue.append(5)
queue.sort()

print(queue.pop(0)) # 0 for lowest -1 for highest

# using Binary heap
from queue import PriorityQueue
q = PriorityQueue()
q.put(10)
q.put(20)
q.put(100)
q.put(5)
print(q.get())

# using tuple

q = []
q.append((1,"alexa"))
q.append((3,"ale"))
q.append((2,"al"))

q.sort(reverse=True)
print(q)


# using heapq
import heapq
pq = []
heapq.heappush(pq, (1, "Low Priority Task"))
heapq.heappush(pq, (0, "High Priority Task"))
print(heapq.heappop(pq))
