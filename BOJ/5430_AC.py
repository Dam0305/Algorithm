from collections import deque
n = int(input())

for i in range(n):
    order = list(input())
    size = int(input())
    a = input()
    tmp = ''
    arr = deque([])
    idx = 0
    for i in a:

        if i in ',]':
            arr.append(tmp)
            tmp = ''
        elif i == '[':
            continue
        else:
            tmp += i
    if order.count('D') > size:
        print('error')
    else:
        for j in order:
            if j == 'R': #0이면 정순 1이면 역순
                idx = 1 if idx == 0 else 0
            elif j == 'D':
                if idx ==1 :
                    arr.pop()
                else:
                    arr.popleft()
        arr = list(arr)
        print('[' + ','.join(arr if order.count('R')%2 == 0 else arr[::-1]) + ']')
