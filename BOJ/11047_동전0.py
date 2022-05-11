def solution(k, coins):
    answer = 0
    # 큰 동전부터 해결하기 위해 내림차순 정렬
    coins.sort(reverse=True)

    for i in coins:
        # 큰 동전부터 k와 비교하여 k가 더 큰 경우
        if i <= k:
            # 몫은 동전 개수, 나머지는 다시 계산
            answer += k // i
            k %= i

            if k == 0:
                break

    print(answer)


n, k = input().split()
arr = []
for i in range(int(n)):
    arr.append(int(input()))

solution(int(k), arr)
