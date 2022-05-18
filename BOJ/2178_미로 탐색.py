from collections import deque


def bfs(n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나거나 0인 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            elif maze[nx][ny] == 0:
                continue

            # 1인 경우 큐에 삽입하고 현재 값 + 1로 치환
            elif maze[nx][ny] == 1:
                q.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
    
    #n,m 값 반환해주면 최소값 반환해줄 수 있음
    return maze[-1][-1]


n, m = map(int, input().split())
maze = [[] for _ in range(n)]

for i in range(n):
    maze[i] = list(map(int, (' '.join(input())).split()))

print(bfs(n, m))
