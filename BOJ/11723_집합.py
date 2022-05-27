import sys


m = int(input())
arr = [0]*21
n = 0

for i in range(m):
    order = sys.stdin.readline().strip() #개행 지워줘야함

    if order != 'all' and order != 'empty':
        order, n = order.split()
        n = int(n)

    if order == 'add':
        if arr[n] == 0: arr[n] = 1

    elif order == 'remove':
        if arr[n] == 1: arr[n] = 0

    elif order == 'check':
        print(arr[n])

    elif order == 'toggle':
        arr[n] = 0 if arr[n] == 1 else 1

    elif order == 'all':
        arr = [1]*21

    elif order == 'empty':
        arr = [0]*21

    #print(arr)
