import heapq
INF = int(1e9)

def dilkstra(start):
    q = []
    heapq.heappush(q, [0, start])

    distance[start] = 0 #시작 노드 거리 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: #방문했던 노드 무시
            continue

        for i in graph[now]:
            cost = dist + i[1] #노드 거리 계산

            if cost < distance[i[0]]: #더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    return 0


n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF]*(n+1) #거리 초기화

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

dilkstra(start)

for i in range(1, n + 1):
    if distance[i]== INF:
        print("INF")
    else:
        print(distance[i])
