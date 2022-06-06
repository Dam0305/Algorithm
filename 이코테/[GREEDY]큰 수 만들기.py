def solution(number, k):
    arr = []
    for i in number:
        if len(arr) == 0:
            arr.append(i)
            continue

        if k > 0:
            while arr[-1] < i:
                arr.pop()
                k -= 1
                if len(arr) == 0 or k <= 0:
                    break
        arr.append(i)

    return ''.join(arr[:len(arr) - k])
