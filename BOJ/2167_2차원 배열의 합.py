n,m = map(int, input().split())
arr = [[0 for _ in range(m+1)]] #인덱스 범위 벗어나는 것 방지

for i in range(n):
    arr.append([0] + list(map(int, input().split())))


for i in range(1, n+1):
    for j in range(1, m+1):
        #누적합 구하기
        arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i][j] - arr[i-1][j-1]

n = int(input())

for _ in range(n):
    i,j,x,y = map(int, input().split())
    #범위 계산
    print(arr[x][y]-arr[x][j-1]-arr[i-1][y]+arr[i-1][j-1])
