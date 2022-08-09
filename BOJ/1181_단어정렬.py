n = int(input())

arr = [input() for _ in range(n)]

arr = list(set(arr)) #중복 제거
arr.sort() #사전 순
arr.sort(key=len) # 길이순

for i in arr:
    print(i)