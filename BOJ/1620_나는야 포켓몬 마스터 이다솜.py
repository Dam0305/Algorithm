import sys

n, m = map(int, input().split())

name = {}
num = {}
for i in range(1, n+1):
    a = sys.stdin.readline().strip()
    name[a] = i
    num[i] = a


for i in range(m):
    a = sys.stdin.readline().strip()
    if a[0] in '0123456789':
        print(num[int(a)])
    else:
        print(name[a])
