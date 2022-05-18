def dfs(x, y, c): #탐색할 위치와 단지 나타내는 변수
    
    #범위 벗어나면 바로 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    # 위치 값이 1이면 아직 방문하지 않은 위치
    if city[x][y] == 1:
        #같은 단지임을 나타내기 위한 같은 수로 마킹
        city[x][y] = c
        
        #상하좌우 확인
        dfs(x-1, y, c)
        dfs(x + 1, y, c)
        dfs(x, y-1, c)
        dfs(x, y+1, c)
        return True #연결된 곳 모두 방문하였으면 True

    return False



cnt = 0
c = 2 #같은 단지 표시 위한 변수(1로 단지가 표시되어있으므로 2부터 시작)
n = int(input())
city = [[] for _ in range(n)]

for i in range(n):
    city[i] = list(map(int, (' '.join(input())).split()))


for i in range(n):
    for j in range(n):
        if dfs(i, j, c): #탐색 결과가 True면
            cnt += 1 #단지수 증가
            c += 1 #다른 단지를 나타내기 위해 1 증가

result = [0 for _ in range(c)] 

for j in range(2, c):
    for i in city:
        result[j] += i.count(j) #같은 수로 마킹된 위치 개수 확인

result.sort()
print(cnt) #단지 수 출력
for i in result:
    if i != 0:
        print(i) #각 단지마다 가구 수 출력
