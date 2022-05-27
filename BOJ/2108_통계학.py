from collections import Counter
import sys

n = int(input())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()#오름차순 정렬
dic = Counter(arr).most_common() #빈도수 체크


print("%d\n%d\n%d\n%d" % (round(sum(arr) / n), #평균(반올림)
                          arr[n // 2], #중앙값
                          dic[1][0] if len(arr) > 1 and dic[0][1] == dic[1][1] else dic[0][0], #최빈값 여러개면 최빈값 중 두번째로 작은 수
                          max(arr) - min(arr))) #최대값-최소값                                    (오름차순 정렬 후 빈도수 체크했기 때문에 다음 값이 두번째로 작은 값)
