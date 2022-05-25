n = int(input())

arr = []

for i in range(n):
    target = int(input())
    if target != 0: #0 이 아니면 리스트에 추가
        arr.append(target)
    elif target == 0:# 0이면
        if len(arr) != 0: #리스트에 원소가 있는지 확인 후 있으면 추출
            arr.pop()
        else: #없으면 추가
            arr.append(target)

print(sum(arr)) #합계 출력
