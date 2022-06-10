from collections import deque
import sys

t = int(input())
n = 0
d = deque([])
for _ in range(t):
    order = sys.stdin.readline().strip()
    if 'push' in order:
        order, n = order.split()
        if 'front' in order:
            d.insert(0, int(n))
        elif 'back' in order:
            d.append(int(n))
    elif 'pop' in order:
        if 'front' in order:
            print(d.popleft() if len(d) != 0 else -1)
        elif 'back' in order:
            print(d.pop() if len(d) != 0 else -1)
    elif order == 'front': print(d[0] if len(d) != 0 else -1)
    elif order == 'back': print(d[-1] if len(d) != 0 else -1)
    elif order == 'size': print(len(d))
    elif order == 'empty': print(0 if len(d) != 0 else 1)
