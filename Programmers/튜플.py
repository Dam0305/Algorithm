def solution(s):
    #문자열에서 괄호 없애고 쉼표로 나눠서 리스트 생성
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.split(',')
    dic = {}

    #리스트 순회하면서 딕셔너리에 넣고 카운트
    #from collections import Counter 라이브러리 사용했으면 빠르게 풀 수 있었음
    for i in s:
        if i not in dic:
            dic[i] = 1
        elif i in dic:
            dic[i] += 1

    answer = [0 for _ in range(len(dic))]
    #딕셔너리에서 추출하면서 등장한 횟수를 인덱스로 삽입
    for e, i in dic.items():
        answer[i - 1] = int(e)
    #적게 등장한 숫자가 앞에 있으므로 역순으로 뒤집어줌
    answer = answer[::-1]

    return answer

'''
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4])
print(solution("{{123}}"))'''
