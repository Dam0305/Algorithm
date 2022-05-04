def solution(p):
    cnt = 0
    # 빈 문자열이면 빈 문자열 반환
    if p == '': return ''

    u, v = '', ''
    #괄호 확인하면서 짝이 맞는 괄호가 u
    for i in p:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        u += i
        if cnt == 0:
            break

    #나머지의 괄호가 v
    v = p[len(u):]

    #u가 (로 시작한다면 올바른 괄호이므로 u+ 재귀함수 (v)
    if u[0] == '(':
        return u + solution(v)
    #올바른 괄호가 아니라면
    else:
        #4-1 단계
        tmp = '('
        #4-4단계
        u = u[1:-1]
        if len(u) != 0:
            u = list(u)
            for i in range(len(u)):
                if u[i] =='(':
                    u[i] = ')'
                elif u[i] ==')':
                    u[i] = '('
            u = ''.join(u)
        #4-2, 4-3, 4-5 단계
        return tmp + solution(v)+ ')' + u
