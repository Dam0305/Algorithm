n = int(input())
m = int(input())

arr = []

#소수판변
def prime(n):
    import math

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


for i in range(n, m+1):
    if prime(i): #소수이면 리스트에 삽입
        arr.append(i)

#1은 소수가 아니므로 존재하면 삭제
if 1 in arr: arr.remove(1)

#소수 없으면 -1 출력
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
