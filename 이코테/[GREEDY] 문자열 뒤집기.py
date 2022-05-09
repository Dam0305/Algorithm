def solution(s):

    move = 0
    target = s[0]
    if s.count('0') == 0 or s.count('1') == 0:
        return 0

    for i in range(len(s)-1):
        if s[i] != s[i+1] and s[i+1] != target:
            move += 1

    return move
