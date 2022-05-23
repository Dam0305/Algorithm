INF = int(1e9)

n = int(input())
m = int(input())
g = [[INF] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            g[i][j] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    if c < g[a][b]:
        g[a][b] = c


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if g[i][j] == INF:
            print(0, end=' ')
        else:
            print(g[i][j], end=' ')
    print()
