
n,k = map(int, input().split())

def solution(n, k):
    cnt = 0
    arr = [i for i in range(2, n+1)]

    while arr:
         #제일 작은 수 찾아서 삭제하고
        p = min(arr)
        arr.remove(p)
        cnt += 1 #삭제한 순서 증가

        if cnt == k: #찾고 있는 순서면 지운 수 반환
            return p

        
        i = 0
        while True:
            #배열에 있는 p의 배수 삭제
            if arr[i] % p == 0:
                cnt += 1
                if cnt == k: #찾고 있는 순서면 반환
                    return arr[i]
                arr.pop(i)
            i += 1
            if i >= len(arr):
                break

print(solution(n,k))
