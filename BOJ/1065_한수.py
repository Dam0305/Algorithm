def solution(n):
    cnt = 0
    if n < 100: #100 미만이면 한수는 n개
        return n
    else:
        cnt = 99 #100이면 한수가 99개이므로 99부터 시작
        for i in range(100, n+1):
            a = i //100 #100의 자리
            b = (i//10)%10 #10의 자리
            c = i%10 #1의 자리
            
            #그 차이가 같으면 한수
            if a - b == b-c:
                cnt += 1

        return cnt

n = int(input())
print(solution(n))
