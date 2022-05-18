def solution(arr, target):
    l = 0
    r = max(arr)
    answer = 0

    while l <= r:
        wood = 0
        mid = (l + r) // 2

        for i in arr:
            if i > mid:
                wood += i - mid  # 벌목하고 난 후 나무 길이 합

        if wood == target:  # 나무 길이 합과 원하는 양이 같으면
            return mid  # 높이 반환

        elif wood > target:  # 나무 길이 합이 더 크면
            l = mid + 1  # 시작 크기 늘려서 범위 반으로 줄임
            answer = mid  # 최대한 덜 잘라야하므로 저장해둠

        elif wood < target:  # 나무 길이 합이 더 작으면 종료 크기 줄여서 왼쪽 탐색
            r = mid - 1

    return answer


n, target = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(arr, target))
