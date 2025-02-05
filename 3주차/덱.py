from sys import stdin
from collections import deque

n = int(stdin.readline())
deq = deque()

for i in range(n):
    order = stdin.readline().split()

    if order[0] == 'push_front': 
        deq.appendleft(order[1])

    elif order[0] == 'push_back': 
        deq.append(order[1])

    elif order[0] == 'pop_front': 
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())

    elif order[0] == 'pop_back': 
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())

    elif order[0] == 'size': 
        print(len(deq))

    elif order[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])

    elif order[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])