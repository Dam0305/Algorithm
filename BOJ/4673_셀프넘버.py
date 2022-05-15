def solution():

    self_num = set(range(1, 10001)) #전체 수
    num = set() #셀프넘버가 아닌 수를 저장할 집합

    for i in range(1, 10001):
        for j in str(i): #문자열로 나눠서 각 자리 더해줌
            i += int(j)

        num.add(i)

    self_num -= num #전체 수에서 셀프 넘버가 아닌 수를 빼줌
    #오름차순으로 정렬 후 출력
    for i in sorted(self_num):
        print(i)
solution()
