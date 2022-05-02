def solution(answers):
    #스코어 저장하기 위해 0으로 초기화
    answer = [0 * _ for _ in range(3)]

    #학생들의 답안 찍는 주기
    students = [[1,2,3,4,5],
                [2,1,2,3,2,4,2,5],
                [3,3,1,1,2,2,4,4,5,5]]

    #학생마다 답안 찍는 주기가 다르므로 answers의 크기로 맞춰줌
    #이럴 경우엔 enumerate 사용!
    for i in range(3):
        if len(students[i]) < len(answers):
            for j in range((len(answers))- len(students[i])):
                students[i].append(students[i][j])

    #정답만큼 반복하면서 정답 확인
    for i in range(len(answers)):
        #answer 각 인덱스 값에 정답만큼 값을 올려줌
        if students[0][i] == answers[i]:
            answer[0] += 1
        if students[1][i] == answers[i]:
            answer[1] += 1
        if students[2][i] == answers[i]:
            answer[2] += 1

    #print('answer->', answer)

    #스코어의 max의 개수가 2 이상이라면 정답의 개수가 모두 같으므로
    if answer.count(max(answer)) > 2:
        #123 반환
        return [1,2,3]

    #스코어의 max의 개수가 1 이상이라면 2명의 학생의 정닶 개수가 같으므로
    if answer.count(max(answer)) > 1:
        #값을 기준으로 정렬하지만 인덱스 값으로 치환해줌
        #정답은 1,2,3 으로 나와야하기 때문에 0인덱스에 0값을 삽입
        answer.insert(0, 0)
        answer = sorted(range(len(answer)), key= lambda k: answer[k], reverse=True)
        #0값과 정닶의 개수가 max가 아닌 것들이 뒤에 있으므로 두 번의 pop
        answer.pop()
        answer.pop()
        return answer

    #정답의 개수가 가장 많은 학생이 한 명이라면 해당 학생의 인덱스에 +1을 해주며 반환
    return [answer.index(max(answer))+1]
