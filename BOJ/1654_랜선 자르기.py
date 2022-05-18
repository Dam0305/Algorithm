def solution(arr, target):
    answer = 0
    l = 0
    r = max(arr)
    
    while l <= r:
        mid = (l + r) // 2
        
        if mid == 0: mid = 1 #나눠서 개수를 찾아야하기 때문에 mid가 0이 되면 안된다
        
        cnt= 0
        
        #현재 mid cm로 만들 수 있는 랜선 개수
        for i in arr:
            cnt += i // mid

        if cnt >= target: #개수가 크거나 같으면 길이 저장해두고 오른쪽 탐색
            l = mid + 1
            answer = mid
            
        elif cnt < target: #개수가 작으면 왼쪽 탐색
            r = mid - 1

    return answer


n, target = map(int, input().split())
arr = [int(input()) for _ in range(n)]

print(solution(arr, target))
