# 첫번째 문제 풀이
# 큰 수의 카드를 뽑고 그 카드가 속한 그룹에서 제일 작은 수가 가장 큰 것을 찾는 게임
def first(cards):
    num = 0
    
    #2차원 리스트에서 제일 작은 것 중 큰 것을 찾음
    for i in range(len(cards)):
        if num < min(cards[i]):
            num = min(cards[i])
    return num
