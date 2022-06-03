def prim(a):
    import math
    n = a*2

    arr = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]:
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j += 1


    return arr


while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    arr = prim(n)


    print(arr[n+1:n*2+1].count(True))
