import sys

n = int(sys.stdin.readline())

arr = [0 for _ in range(100001)]

#계수 정렬
for _ in range(n):
    i = int(sys.stdin.readline())
    arr[i] += 1


for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)
