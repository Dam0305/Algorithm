import heapq #파이썬은 최소힙이므로 삽입, 출력 시 - 부호 붙여주어 최대힙처럼 사용 가능
import sys

q = []
t = int(input())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print(0 if len(q) == 0 else -heapq.heappop(q)) #출력할 때 -를 붙여주어 원래대로 출력
    else:
        heapq.heappush(q,-n) #최소힙이므로 -로 삽입

