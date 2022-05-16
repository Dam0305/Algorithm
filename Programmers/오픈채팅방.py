def solution(record):
    answer = []
    users = {}
    id = []
    message = []

    for i in record:
        i = str(i).split()
        action = i[0] #유저의 행동
        if action == "Enter":
            users[i[1]] = i[2] #유저아이디는 고유하므로 유저아이디를 key로, 닉네임을 value로 dict 자료형에 저장
            id.append(i[1]) #id 리스트에 현재 유저 아이디 삽입
            message.append("님이 들어왔습니다.") #메세지 리스트에 현재 유저의 행동 메세지 삽입
        elif action == "Leave":
            id.append(i[1])
            message.append("님이 나갔습니다.")
        elif action == "Change":
            users[i[1]] = i[2] #dict의 value 수정

    #id와 message의 리스트를 동시에 순회하여 id에 맞는 닉네임을 찾아서 answer 리스트에 삽입
    for i, j in zip(id, message):
        answer.append(users[i]+ j)

    return answer

print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
