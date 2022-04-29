def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    dic = {id: 0 for id in id_list}
    report = set(report)
    name_list = set()
    for i in report:
        i = str(i).split()
        if i[1] in dic.keys():
            dic[i[1]] += 1

    for key, value in dic.items():
        if k <= value:
            name_list.add(key)

    for i in report:
        i = str(i).split()
        if i[1] in name_list:
            answer[id_list.index(i[0])] += 1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
               2))
