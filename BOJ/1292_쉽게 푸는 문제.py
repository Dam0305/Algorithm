n, m = map(int, input().split())

i = 1 #수열 만들 변수
cnt = 1 #수열 개수 체크할 변수

#누적합 리스트
arr = [0]

for _ in range(m):
    #이전 값을 더해서 추가
    arr.append(arr[-1] +i)

    #숫자가 같은 수만큼 리스트에 삽입 됐으면 숫자 증가
    if cnt == i:
        cnt = 0
        i+=1
    #삽입하고 숫자 횟수 증가
    cnt += 1

#구간합 출력
print(arr[m]-arr[n-1])
