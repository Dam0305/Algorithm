def solution(s):
    arr = []

    s = list(s)
    for i in range(1, len(s)):
        # 압축 문자열 담을 변수
        tmp = ''
        # 동일 문자 확인하기 위한 인덱스 2개
        l, r = 0, 0
        # 압축 길이 변수
        cnt = 1
        while r < len(s):
            # i의 크기가 압축 단위
            r += i
            if s[l:r] == s[r:r + i]:
                cnt += 1
            elif s[l:r] != s[r:r + i]:
                if cnt == 1:
                    tmp += ''.join(s[l:r])
                elif cnt != 1:
                    tmp = tmp + str(cnt) + ''.join(s[l:r])
                    cnt = 1

            l = r
        arr.insert(i,tmp)
        print(arr)
    return len(min(arr, key=len))
