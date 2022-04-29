cnt = int(input())

while cnt != 0:
    order = input()
    order = order.split()
    n = int(order[0])
    word = order[1]
    for i in word:
        for j in range(n):
            print(i, end="")
    print()
    cnt -= 1
