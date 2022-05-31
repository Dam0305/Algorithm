n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))

def check(i):
    l = 0
    r = len(arr1) - 1
    while l <= r:
        mid = (l + r) // 2

        if arr1[mid] == i:
            return True
        elif arr1[mid] > i:
            r = mid - 1
        elif arr1[mid] < i:
            l = mid + 1
    return False

for i in arr2:
    print(1 if check(i) else 0, end=' ')


