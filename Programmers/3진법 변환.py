def solution(n):
    answer = 0

    #결과 저장할 리스트
    s = []

    while n != 0:
        #나머지값 저장
        s.append(str(n%3))
        #몫은 다시 사용
        n = n//3

    #역순으로 저장
    #인덱스 사용해서 3진법 계산 위함
    s = ''.join(s[::-1])

    #인덱스 사용해서 3진법 계산
    for i in range(len(s)):
        answer = answer + (int(s[i])*(3**i))

    #int(s, 3)으로 출력하면 문자열이 3진법으로 출력된다고 함
    return answer
