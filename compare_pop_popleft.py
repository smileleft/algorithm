from collections import deque
import time

lst = list(range(100000))
dq = deque(range(100000))

start_time = time.time()
for i in range(100000):
    lst.pop(0)
print("pop(0) 소요시간: ", time.time() - start_time)

start_time = time.time()
for i in range(100000):
    dq.popleft()
print("deque popleft() 소요시긴: ", time.time() - start_time)