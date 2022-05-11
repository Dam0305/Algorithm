def solution(N):
    answer = 0

    while N >= 0:
        #5의 배수이면
        if N % 5 == 0:
            #N에서 5를 뺀 몫을 더해주고 반복문 탈출
            answer += N // 5
            print(answer)
            break
        #5의 배수가 아니라면 3을 빼면서 5의 배수로 만들어줌
        N -= 3
        answer += 1

    if N != 0: #N을 정확하게 나눌 수 없을 경우
        print(-1)
