def solution(expression):

    #경우의 수 저장
    arr = [['*', '+', '-'], ['*', '-', '+'],
           ['+', '-', '*'], ['+', '*', '-'],
           ['-', '*', '+'], ['-', '+', '*']]

    # 문자열 피연산자와 연산자로 나눠서 리스트로 저장
    def tran(s):
        ex = []
        tmp = ''
        for i in expression:
            if i not in arr[0]:
                tmp += i
            elif i in arr[0]:
                ex.append(tmp)
                ex.append(i)
                tmp = ''
        ex.append(tmp)
        return ex

    #계산 함수
    def cal(n1, n2, op):
        if op == '*':
            return int(n1) * int(n2)
        elif op == '+':
            return int(n1) + int(n2)
        elif op == '-':
            return int(n1) - int(n2)

    #경우의 수 별로 결과 저장할 배열
    result = [0 for _ in range(6)]

    #경우의 수 만큼 반복
    for i in range(len(arr)):
        #연산식 리셋
        ex = tran(expression)
        #경우의 수 안의 우선순위 연산자
        for j in arr[i]:
            #연산자가 있을 때만 반복문 실행
            while j in ex:
                #연산자 앞 뒤의 피연산자와 계산,
                #해당 연산자 자리에 연산 결과 넣기 위해 인덱스 저장
                x = ex.index(j)
                #계산 함수를 통해서 연산 결과 저장
                y = cal(ex[x-1], ex[x+1], j)
                #연산자 자리에 결과로 치환
                ex[x] = y
                #연산자 앞의 피연산자 리스트에서 삭제
                ex.pop(x-1)
                #리스트의 수가 1개 줄었으나 저장된 연산자의 index는 그대로이므로
                #연산자 index = 연산자 다음의 피연산자 자리 => 해당 인덱스 값 삭제
                ex.pop(x)
        #결과를 result 리스트에 넣기 전에 음수이면 양수로 바꿔서 저장
        if ex[0] < 0:
            #int형은 앞에 -하나 더 붙이면 양수로 변환
            ex[0] = -ex[0]
        result[i] = ex[0]


    return max(result)
