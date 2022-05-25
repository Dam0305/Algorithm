n,k = map(int, input().split())

arr = [i for i in range(1, n+1)]
idx = 0
result = []
k -= 1 #인덱스는 0부터 시작하므로 1 감소

while len(arr) != 0:
    idx += k #인덱스 간격
    
    #인덱스가 리스트 범위를 벗어나면
    if idx >= len(arr):
        #리스트 범위 안으로 들어올 때까지 리스트 길이를 빼줌
        while idx >= len(arr):
            idx -= len(arr)
    
    #현재 인덱스가 위치한 리스트의 값을 순열 리스트에 추가하고 원본 리스트에서 제거
    result.append(arr[idx])
    arr.pop(idx)

#결과 출력
print('<'+ ', '.join(list(map(str, result)))+'>')
