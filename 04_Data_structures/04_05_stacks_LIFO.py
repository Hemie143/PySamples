# list
s = []
s.append('eat')
s.append('sleep')
s.append('work')
print(s)                    # ['eat', 'sleep', 'work']
print(s.pop())              # work
print(s.pop())              # sleep
print(s.pop())              # eat
# print(s.pop())              # IndexError: pop from empty list

# collections.deque
from collections import deque
s = deque()
s.append('eat')
s.append('sleep')
s.append('work')
print(s)                    # deque(['eat', 'sleep', 'work'])
print(s.pop())              # work
print(s.pop())              # sleep
print(s.pop())              # eat
# print(s.pop())              # IndexError: pop from an empty deque

# queue.LifoQueue
from queue import LifoQueue
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('work')
print(s)                    # <queue.LifoQueue object at 0x00000174DA32EFD0>
print(s.get())              # work
print(s.get())              # sleep
print(s.get())              # eat
