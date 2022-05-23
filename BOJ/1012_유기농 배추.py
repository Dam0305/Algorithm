import sys

sys.setrecursionlimit(10**6) # 최대재귀깊이 지정 함수


def dfs(x, y):
    global cnt

    # 범위 벗어나면 바로 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 위치 값이 1이면 아직 방문하지 않은 위치
    if board[x][y] == 1:
        # 방문한 결과로 0 으로 초기화
        board[x][y] = 0

        # 상하좌우 확인
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True  # 연결된 곳 모두 방문하였으면 True

    return False


case = int(input())
cnt = 0

while case > 0:
    cnt = 0
    m,n,k = map(int, input().split())

    board = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        a,b = map(int, input().split())
        board[b][a] = 1



    for i in range(n):
        for j in range(m):
            if dfs(i, j):  # 탐색 결과가 True면
                cnt += 1  # 마리 수 + 1

    case -= 1
    print(cnt)
