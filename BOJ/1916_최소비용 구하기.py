import heapq

INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)
        distance[start] = 0

        if distance[now] < dist:
            continue
        for i in g[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return 0


n = int(input())
m = int(input())

g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])

start, end = map(int, input().split())
distance = [INF] * (n + 1)

dijkstra(start)

print(distance[end])
