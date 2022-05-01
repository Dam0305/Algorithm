

def solution(numbers, hand):
    answer = ''
    #키패드 좌표
    p = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2],
         7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}

    #시작 위치
    l = [3,0]
    r = [3,2]

    #거리 계산하기 위한 함수
    def subMat(a, b):
        #이동하는 것이 아니라 거리 계산만 하면 되기 때문에 절댓값으로 반환
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    #num만큼 반복
    for i in numbers:
        #y값이 0이면 왼손으로 입력
        if p[i][1] == 0:
            l = p[i]
            answer += 'L'
        #y값이 2이면 오른손으로 입력
        elif p[i][1] == 2:
            r = p[i]
            answer += 'R'
        #y값이 1이면
        elif p[i][1] == 1:
            #숫자와 손가락의 거리 계산 후 왼손과의 거리가 더 멀면
            if subMat(p[i], l) > subMat(p[i], r):
                #오른손이 입력
                answer += 'R'
                r = p[i]
            #오른손과의 거리가 더 멀면
            elif subMat(p[i], l) < subMat(p[i], r):
                #왼손이 입력
                answer += 'L'
                l = p[i]
            #같을 경우 손잡이 확인 후 결정
            elif subMat(p[i], l) == subMat(p[i], r):
                if hand == "right":
                    r =p[i]
                    answer += 'R'
                elif hand == 'left':
                    l = p[i]
                    answer += 'L'
    print(answer)

    return answer

'''
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") =="LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left') == "LRLLRRLLLRR")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right') == "LLRLLRLLRL")'''
