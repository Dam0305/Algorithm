def solution(x):
    r = x[0]
    c = x[1]
    #나이트가 체스판의 가장자리에 있지 않다면 움직일 수 있는 경우의 수
    cnt = 8
    
    #가장자리에 있는 걸 확인하고 갈 수 없는 경로의 수를 빼준다
    if r in ['a', 'h']:
        cnt -= 4
        if c in ['1', '8']:
            cnt -= 2
        elif c in ['2', '7']:
            cnt -= 1
    elif r in ['b', 'c']:
        cnt -= 2
        if c in ['1', '8']:
            cnt -= 3
        elif c in ['2', '7']:
            cnt -= 2

    return cnt

