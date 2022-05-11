def solution(coins):

    coins.sort()
    target = 1

    for coin in coins:
        #타겟과 코인을 비교해서
        #타겟이 코인이랑 크거나 같으면 코인으로 타겟 만들 수 있음
        if target >= coin:
            #타겟은 코인을 더해서 높여줌
            target += coin
        #타겟이 코인이보다 작으면 코인으로 만들 수 없음
        #그러므로 만들 수 없는 금액은 타겟이 됨
        else:
            return target
