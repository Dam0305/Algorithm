import itertools

def solution(relation):
    #인덱스로 비교하기 위함
    idx = [i for i in range(len(relation[0]))]
    coms = []

    #인덱스 조합
    for i in range(1, len(relation)+1):
        coms.extend(itertools.combinations(idx, i))

    unique = []

    for com in coms:
        tmp = []
        for rel in relation:
            arr = []
            #인덱스와 정보 매칭
            for i in range(len(com)):
                arr.append(rel[com[i]])
            tmp.append(arr)
            
        uni = True
        for t in tmp:
            #유일성 만족 확인
            if tmp.count(t) != 1:
                uni = False

        #유일성 만족하면 최소성 확인
        if uni:
            mini = True
            for item in unique:
                if set(item).issubset(com): #부분집합인지 확인 -> 최소성 확인
                    mini = False
            if mini:
                unique.append(com)
    return len(unique)
