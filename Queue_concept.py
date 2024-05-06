from collections import deque
queue = deque()
# deque  양쪽에서 삽입 및 삭제 가능

queue.append(1)  # queue 
queue.popleft(1)  

queue.appendleft(1)  # reverse 입 출 
queue.pop(1) 