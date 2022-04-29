cnt = int(input())
sum = 0
score = 1
while cnt != 0:
    arr = input()
    for i in arr:
        if i == "O":
            sum += score
            score += 1
        elif i == "X":
            sum += 0
            score = 1

    print(sum)
    score = 1
    sum = 0
    cnt -= 1
