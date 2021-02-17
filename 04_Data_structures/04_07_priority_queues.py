# list
q = []
q.append((2, 'work'))
q.append((1, 'eat'))
q.append((3, 'sleep'))
q.sort(reverse=True)
while q:
    print(q.pop())              # (1, 'eat) - (2, 'work') - (3, 'sleep')

# heapq
import heapq
q = []
heapq.heappush(q, (2, 'work'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))
while q:
    print(heapq.heappop(q))     # (1, 'eat) - (2, 'work') - (3, 'sleep')

# queue.PriorityQueue
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'work'))
q.put((1, 'eat'))
q.put((3, 'sleep'))
while not q.empty():
    print(q.get())              # (1, 'eat) - (2, 'work') - (3, 'sleep')
