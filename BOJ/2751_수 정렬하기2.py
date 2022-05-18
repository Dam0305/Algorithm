import sys

def quick(arr):
    if len(arr) <= 1:
        return arr

    p = arr[-1] #이렇게 지정해서 pivot을 잡으면 최악의 경우 O(n^2)

    left = [x for x in arr if x < p]
    right = [x for x in arr if x > p]

    return quick(left) + [p] + quick(right)


def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #중간 값을 가지고
    #오른쪽 왼쪽 분할
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    l, r = 0, 0
    merged = []
    #분할 된 리스트에서 더 작은 것을 새로운 리스트에 먼저 삽입
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l+=1

        elif left[l] >= right[r]:
            merged.append(right[r])
            r += 1

    #남아있는 리스트 병합
    merged += left[l:]
    merged += right[r:]

    return merged


n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr = merge(arr)

for i in arr:
    print(i)
