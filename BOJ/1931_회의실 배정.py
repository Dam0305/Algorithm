def solution(arr):

    
    arr.sort(key= lambda x:(x[0])) #회의 시작 시각 기준 오름차순 정렬
    arr.sort(key=lambda x:x[1]) #회의 종료 시각 기준 오름차순 정렬
    cnt = 0
    finish = 0
    
    for i in arr:
        #처음 종료 시각 설정
        if finish == 0:
            finish = i[-1]
            cnt += 1
        #종료 시각보다 시작 시각이 더 늦다면 회의실 사용 가능
        elif i[0] >= finish:
            cnt += 1
            finish = i[-1]

    print(cnt)



n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

solution(arr)
