from collections import deque


def bfs(start):
    q = deque([start])

    visited[start] = True  # 시작노드 방문

    cnt = 0

    while q:
        com = q.popleft()
        for i in g[com]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1 #방문할 수 있는 노드 count

    return cnt


n = int(input())
m = int(input())

g = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * n

print(bfs(1))
