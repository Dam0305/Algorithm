n, m = map(int, input().split())


dic = {}
arr = []
for i in range(n):
    dic[input()] = 1

cnt = 0
for i in range(m):
    s = input()
    if s in dic.keys():
        cnt += 1

print(cnt)
