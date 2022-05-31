
n = int(input())


def fibo():
    result = []
    result.insert(0, [1, 0])
    result.insert(1, [0, 1])

    for i in range(2,41):
        result.insert(i, [result[i - 1][0] + result[i - 2][0], result[i - 1][1] + result[i - 2][1]])
    return result

arr = fibo()
for i in range(n):
    print(' '.join(map(str, arr[int(input())])))
