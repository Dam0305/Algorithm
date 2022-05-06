import itertools
from collections import Counter

def solution(orders, course):
    answer = []

    for i in course:
        com = []
        for j in orders:
            com.extend(list(itertools.combinations(sorted(j), i))) #정렬 후 조합
        cnt = Counter(com)
        if cnt:
            #1번의 조합으로만 주문된 것 제외
            if max(cnt.values()) >= 2:
                for k, v in cnt.items():
                    if v == max(cnt.values()):
                        answer.append("".join(k))

    return sorted(answer)
