def solution(nums):
    #폰켓몬의 종류와 한 번에 가질 수 있는 폰켓몬의 개수가 같다면
    if len(set(nums)) >= len(nums)//2:
        #가질 수 있는 폰겟몬의 수 그대로 반환
        return len(nums)//2
    #가질 수 있는 폰켓몬의 수 보다 종류가 적을 때는
    elif len(set(nums)) < len(nums)//2:
        #종류 수 반환
        return len(set(nums))
    return 0
