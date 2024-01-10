
# Queues -> FIFO: FirstIn - FirstOut

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

# checking if queue is empty
if not queue:
    print('empty')