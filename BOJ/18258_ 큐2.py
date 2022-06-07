from collections import deque
import sys

n = int(input())

q = deque()
for i in range(n):
    a = sys.stdin.readline().strip()
    if 'push' in a:
        a, n = a.split()

    if a == 'push':
        q.append(n)
    elif a == 'pop':
        print(-1 if len(q) == 0 else q.popleft())
    elif a == 'size':
        print(len(q))
    elif a == 'empty':
        print(1 if len(q) == 0 else 0)
    elif a == 'front':
        print(-1 if len(q) == 0 else q[0])
    elif a == 'back':
        print(-1 if len(q) == 0 else q[-1])
