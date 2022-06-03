import sys
n = int(input())

arr = list(map(int, input().split()))
dp = [0 for i in range(n+1)]

#누적합 계산
for i in range(1, n+1):
    dp[i] = dp[i-1] + arr[i-1]
    
t = int(input())

for i in range(t):
    a, b = map(int,(sys.stdin.readline().strip()).split())
    #print(sum(arr[a-1:b])) #통과는 하지만 누적합과 비교하면 시간 차이 많이 남
    print(dp[b]-dp[a-1])
