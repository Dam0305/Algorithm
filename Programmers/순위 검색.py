import itertools
from collections import defaultdict


def solution(info, query):
    answer = []
    dic = defaultdict(list)



    for i in info:
        i = i.split()
        for k in range(5):
            for j in itertools.combinations(i[:-1], k): #info로 경우의 수 만들기
                dic[''.join(list(j))].append(int(i[-1])) #경우의 수를 key, 점수를 value


    #value 오름차순 정렬
    for i in dic:
        dic[i].sort()


    for i in range(len(query)):
        query[i] = query[i].split()
        score = int(query[i][-1])
        query[i].remove(query[i][-1]) #쿼리에서 스코어 제거
        query[i] = ''.join(query[i])
        query[i] = query[i].replace('and', '')
        query[i] = query[i].replace('-', '')

        if query[i] in dic:
            scores = dic[query[i]]

            if len(scores) > 0:
                l, r = 0, len(scores)
                while l < r:
                    mid = (l + r) // 2
                    if scores[mid] >= score:
                        r = mid
                    else:
                        l = mid + 1
                answer.append(len(scores) - l)
        else:
            answer.append(0)

    return answer
