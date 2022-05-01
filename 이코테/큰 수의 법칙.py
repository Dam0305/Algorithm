#틀린 답
def solution_fail(N, M, K):
    total = 0
    cnt = 0
    idx = 0

    for i in range(M):
        if cnt != K:
            total += N[idx]
            cnt += 1
            if cnt == K:
                cnt = 1
                if idx == 0:
                    idx = 1
                elif idx == 1:
                    idx = 0

    return total


#입력이 커지면 시간초과
def solution(N, M, K):
    total = 0  # 결과값 저장할 변수
    cnt = 0  # 반복 수 체크하기 위한 변수

    # 역순으로 정렬
    N.sort(reverse=True)

    for i in range(M):
        # K번 반복을 했으면
        if cnt == K:
            # 두 번째로 작은 수를 한 번만 더하고 다시 count하기 위해 cnt값을 0으로 초기화
            total += N[1]
            cnt = 0

        # 아직 K번 반복하지 않았으면
        elif cnt != K:
            # 가장 큰 수를 더하고
            total += N[0]
            # cnt 값을 1 증가
            cnt += 1
    # 최종값 return
    return total

#수열 사용
def solution_sequence(N, M,K):
    N.sort(reverse=True)

    total = (((M / (K+1)) * K) + M % (K+1)) * N[0]
    total += (M - (((M / (K+1)) * K) + M % (K+1))) * N[1]

    return int(total)

print(solution_sequence([2, 4, 5, 4, 6], 8, 3))
