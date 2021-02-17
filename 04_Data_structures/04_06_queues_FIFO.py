# list (slow)
q = []
q.append('eat')
q.append('sleep')
q.append('work')
print(q)                            # ['eat', 'sleep', 'work']
print(q.pop(0))                     # eat
print(q.pop(0))                     # sleep
print(q.pop(0))                     # work

# collections.deque
from collections import deque
q = deque()
q.append('eat')
q.append('sleep')
q.append('work')
print(q)                            # deque(['eat', 'sleep', 'work'])
print(q.popleft())                  # eat
print(q.popleft())                  # sleep
print(q.popleft())                  # work
# print(q.popleft())                  # IndexError: pop from an empty deque

# queue.Queue
from queue import Queue
q = Queue()
q.put('eat')
q.put('sleep')
q.put('work')
print(q)                            # <queue.Queue object at 0x000001556BD0EFD0>
print(q.get())                      # eat
print(q.get())                      # sleep
print(q.get())                      # work

# multiprocessing.Queue
from multiprocessing import Queue
q = Queue()
q.put('eat')
q.put('sleep')
q.put('work')
print(q)                            # <multiprocessing.queues.Queue object at 0x000001556BD0EFA0>
print(q.get())                      # eat
print(q.get())                      # sleep
print(q.get())                      # work
