n, m = map(int, input().split())

n1 = set()
n2 = set()

for i in range(n):
    n1.add(input())

for i in range(m):
    n2.add(input())

same = sorted(list(n1.intersection(n2)))
print(len(same))
for i in same:
    print(i)
