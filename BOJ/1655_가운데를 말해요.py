import heapq
import sys

t = int(input())

minQ = []
maxQ = []

mid = int(input())
print(mid)

for i in range(1, t):
    n = int(sys.stdin.readline().strip())

    if len(minQ) == len(maxQ):
        if mid > n:
            heapq.heappush(maxQ, mid)
            heapq.heappush(minQ, -n)

        else:
            heapq.heappush(maxQ, n)
            heapq.heappush(minQ, -mid)
        mid = -heapq.heappop(minQ)

    else:
        if mid > n:
            heapq.heappush(minQ, -n)
        else:
            heapq.heappush(minQ, -mid)
            heapq.heappush(maxQ, n)
            mid = heapq.heappop(maxQ)

    print(mid)
