def solution(s, n):
    answer = ''

    for i in s:
        #공백일 경우 그대로 사용
        if i == ' ':
            answer += i
        #문자가 대문자인 경우
        #isupper, islower 사용해도 됐었음!!!
        elif i >= 'A' and i <= 'Z':
            #문자의 아스키코드 10진수 값과 n값의 결과가
            # 아스키코드의 10진수 값이 90이 넘어가면
            if ord(i) + n > 90:
                #A로 돌아가기 위해 26을 빼고 더해준다
                answer += chr(ord(i) - 26 + n)
            #넘어가지 않을 경우 n값을 그냥 더해줌
            else:
                answer += chr(ord(i) + n)
        #소문자일 경우
        elif i >= 'a' and i <= 'z':
            if ord(i) + n > 122:
                answer += chr(ord(i) - 26 + n)
            else:
                answer += chr(ord(i) + n)
    return answer
