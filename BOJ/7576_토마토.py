from collections import deque


def bfs(q, b, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나거나 0인 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # elif b[nx][ny] == -1:

            # continue

            # 1인 경우 큐에 삽입하고 현재 값 + 1로 치환
            elif b[nx][ny] == 0:
                q.append((nx, ny))
                b[nx][ny] = b[x][y] + 1


def solution():
    m, n = map(int, input().split())
    q = deque()
    board = [[] for _ in range(n)]

    for i in range(n):
        board[i] = list(map(int, input().split()))

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append([i, j])  # 1은 모두 queue에 삽입

    bfs(q, board, n, m)

    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return -1
            if answer < board[i][j]:
                answer = board[i][j]

    return answer - 1


print(solution())
