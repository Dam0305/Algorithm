def solution(n, arr1, arr2):
    answer = []
    a = []
    b = []

    # 각 배열의 원소를 2진수로 변환
    # bin(문자열) 넣어도 됨!!!!
    for i, j in zip(arr1, arr2):
        tmp1 = ''
        tmp2 = ''
        while i > 0:
            tmp1 = str(i % 2) + tmp1
            i //= 2
        while j > 0:
            tmp2 = str(j % 2) + tmp2
            j //= 2
        #2진수로 변환된 문자열 길이가 n보다 작으면 n만큼으로 맞춰줌
        #ljust(문자열, 채울 문자) 사용해도 됨!!!
        if len(tmp1) != n or len(tmp2) != n:
            while len(tmp1) != n:
                tmp1 = '0' + tmp1
            while len(tmp2) != n:
                tmp2 = '0' + tmp2
        #각 배열에 저장
        a.append(tmp1)
        b.append(tmp2)
    
    #2진수로 변환된 리스트에서 
    for i, j in zip(a, b):
        tmp = ''
        for k, l in zip(i, j):
            #두 원소가 1이면 #으로 변환
            if k == '1' or l == '1':
                tmp += '#'
            #둘 다 0이면 공백으로 변환
            elif k == '0' and l == '0':
                tmp += ' '
        #변환한 문자열 저장
        answer.append(tmp)
    
    return answer
