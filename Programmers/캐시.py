def solution(cacheSize, cities):
    answer = 0
    c = []
    t = [10000 for _ in range(cacheSize)]

    if cacheSize == 0:
        return 5*len(cities)

    for i in range(len(cities)):
        cities[i] = cities[i].upper() #대문자로 맞춰줌

        if cities[i] in c: #캐시 안에 존재
            idx = c.index(cities[i]) #가장 옛날에 접근했던 데이터 추출 위해 time 리스트에 접근한 시기 저장
            t[idx] = i
            answer += 1 #hit

        elif cities[i] not in c:
            answer += 5 #캐시에 없으면 miss
            if len(c) != cacheSize: #캐시에 공간 있으면 적재
                c.append(cities[i])
                idx = c.index(cities[i])
                t[idx] = i

            elif len(c) == cacheSize: #캐시에 공간 없으면 제일 옛날에 접근했던 데이터 삭제 후 현재 데이터 적재
                old_idx = t.index(min(t)) #접근 시간이 작을수록 접근한 지 오래 된 데이터
                c[old_idx] = cities[i]
                t[old_idx] = i

    return answer
