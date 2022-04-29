cnt = int(input())

while cnt != 0:
    s = []

    paren = input()
    for i in range(len(paren)):
        #print(s)
        if paren[i] == "(":
            s.append(paren[i])
        elif paren[i] == ")":
            if len(s) != 0 and s[-1] == "(":
                s.pop()
                if len(s) == 0 and i+1 is len(paren):
                    print("YES")
            elif len(s) == 0:
                print("NO")
                break
        if not len(s) == 0 and i+1 == len(paren):
            print("NO")


    cnt -= 1
