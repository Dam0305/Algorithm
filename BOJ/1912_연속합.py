
def solution(n):
    dp = [-1001 for i in range(n+1)]

    arr = list(map(int, input().split()))
    arr.insert(0,0)


    for i in range(1, n+1):
        dp[i] = max(arr[i]+dp[i-1], arr[i])

    return max(dp)

n = int(input())
print(solution(n))
