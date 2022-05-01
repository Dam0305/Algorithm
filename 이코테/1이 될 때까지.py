#첫번째 solution
#문제를 보자마자 반복문으로 풀었고 문제 해결은 되지만 효율성 실패
def first(n, k):
    cnt = 0
    while n > 1:
        if n < k:
            break
        if n % k != 0:
            num = n%k
            n -= num
            cnt += num
        if n%k == 0:
            while True:
                if n < k or n%k != 0:
                    break
                n = n//k
                cnt += 1

    cnt += (n-1)
    return cnt

#두번째solution
#수열을 이용해서 문제 풀이
def second(n, k):
    cnt = 0
    while True:
        num = n%k
        n -= num
        cnt += num
        if n < k:
            break
        cnt += 1
        n //= k

    cnt += (n - 1)

    return cnt

print("re", first(25, 3))
print(second(25, 3))
