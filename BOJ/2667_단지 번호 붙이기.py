
def dfs(x, y): #탐색할 위치와 단지 나타내는 변수
    global cnt #가구 수 계수를 위한 변수

    #범위 벗어나면 바로 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    # 위치 값이 1이면 아직 방문하지 않은 위치
    if city[x][y] == 1:
        #방문한 결과로 0 으로 초기화
        city[x][y] = 0
        cnt += 1 #가구 수 증가
        
        #상하좌우 확인
        dfs(x-1, y)
        dfs(x + 1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True #연결된 곳 모두 방문하였으면 True

    return False


result = []
cnt = 0

n = int(input())
city = [[] for _ in range(n)]

for i in range(n):
    city[i] = list(map(int, (' '.join(input())).split()))


for i in range(n):
    for j in range(n):
        if dfs(i, j): #탐색 결과가 True면
            result.append(cnt) #가구 수 저장
            cnt = 0 #단지 안의 가구 수 초기화


result.sort()
print(len(result)) #단지 수 출력
for i in result:
    print(i) #각 단지마다 가구 수 출력
