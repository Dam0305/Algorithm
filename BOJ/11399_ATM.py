def solution(times):
    temp = 0
    total = 0

    # 오름차순 정렬
    times.sort()

    for i in times:
        total += temp + i
        temp += i

    print(total)


n = input()
arr = input()
arr = list((map(int, arr.split())))
solution(arr)
