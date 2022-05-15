def solution(a):
    cnt = 0
    n = 2
    for i in a:
        n = 2
        if i == 1:
            continue
        else:
            while True:
                if i == n:
                    cnt += 1
                    break
                if i %n ==0: #자기 자신 이전에 나눠지는 수가 있으면 소수가 아님
                    break
                n+= 1
    return cnt

n = int(input())
arr = list(map(int, input().split()))
print(solution(arr))
