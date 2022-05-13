def solution(a, b):

    total = 0
    max, min = -1, 101
    
    while b:
        for i in b:
            if i > max:
                max = i

        for i in a:
            if i < min:
                min = i

        total += max * min #가장 큰 값과 가장 작은 값을 곱한 후 더해야 최소값 만들 수 있음
        b.remove(max) #중복 피하기 위하여 리스트에서 삭제
        a.remove(min)
        max, min = -1, 101

    print(total)



#solution([1,1,1,6,0], [2,7,8,3,1])

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
solution(a, b)
