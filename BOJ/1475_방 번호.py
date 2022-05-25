num = '1234567890'

cnt = 1
n = list(input())

tmp = num

for i in n:
    #방 번호 중 6이나 9가 있으면
    if i == '6' or i == '9':
        #스티커에 없는 숫자로 치환
        i = '6' if '9' not in tmp else '9'

    #방 번호가 스티커에 없으면
    if i not in tmp:
        #스티거 1개 추가
        tmp = tmp + num
        cnt += 1

    #사용한 스티커 처리
    tmp = tmp.replace(i, '-', 1)

print(cnt)
