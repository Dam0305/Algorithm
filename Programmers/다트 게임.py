def solution(dartResult):
    #각 회차 별 점수 담을 리스트
    answer = [0 for _ in range(3)]
    num = '1234567890'
    bonus = {'S': 1, 'D': 2, 'T': 3}
    idx = 0

    #게임횟수만큼 반복
    for i in range(3):
        #input 리스트에 숫자가 있으면
        if dartResult[idx] in num:
            #결과 리스트에 저장
            answer[i] = int(dartResult[idx])
            #10일 경우
            if dartResult[idx] == '1' and dartResult[idx + 1] == '0':
                answer[i] = 10
                #두자리 수이면 인덱스 2번 증가
                idx += 1
            idx += 1

        #보너스 점수 계산
        if dartResult[idx] in bonus:
            #저장된 스코어에 제곱
            answer[i] **= bonus[dartResult[idx]]
            #인덱스 증가
            idx += 1
            #증가한 인덱스가 입력받은 문자열보다 크거나 같으면 점수 계산 종료
            if idx >= len(dartResult):
                break
                
        #옵션 점수 계산
        #스타상이면
        if dartResult[idx] == '*':
            #현재 점수와 이전 점수 2배
            answer[i] *= 2
            answer[i-1] *= 2
            idx +=1
        
        #아차상이면
        elif dartResult[idx] == '#':
            #현재 점수 마이너스
            answer[i] *= -1
            idx += 1

    #합계 반환
    return sum(answer)

'''
print(solution('1S2D*3T'))
print(solution('1D2S#10S'))'''
