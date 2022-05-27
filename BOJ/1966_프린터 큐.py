n = int(input())


for i in range(n):
    cnt, loc= map(int, input().split())
    pri = list(map(int, input().split())) #우선순위

    q = [i for i in range(cnt)] #인덱스
    seq = 0 #출력 순서

    while True:
        if pri[0] == max(pri): #제일 큰 값
            seq += 1 #출력 순서 증가

            if q[0] == loc: #현재 출력물이 찾던 값이면
                print(seq) #순서 출력
                break

            else: #그렇지 않으면 큐에서 삭제
                pri.pop(0)
                q.pop(0)

        else: #제일 큰 값이 아니면 큐의 맨 뒤로 이동
            pri.append(pri.pop(0))
            q.append(q.pop(0))

