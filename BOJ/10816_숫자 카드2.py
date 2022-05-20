import sys

def lowerBound(arr, target):
    l = 0
    r = len(arr)

    while l < r:
        mid = (l+r) // 2

        if arr[mid] >= target: r = mid
        else:nl = mid + 1

    return l

  
def upperBound(arr, target):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l+r) // 2
        if arr[mid] <= target: l = mid + 1
        else: r = mid

    return r


n = int(input())
card1 = list(map(int, sys.stdin.readline().split()))

m = int(input())
card2 = list(map(int, sys.stdin.readline().split()))

card1.sort()


answer = [0 for _ in range(m)]

for i in range(len(card2)):
    #upperbound 인덱스 - lowerbound 인덱스 = 중복 값 개수
    answer[i] = upperBound(card1, card2[i]) - lowerBound(card1, card2[i])

print(' '.join(list(map(str, answer))))


