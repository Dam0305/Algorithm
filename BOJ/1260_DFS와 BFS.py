from collections import deque


def dfs(g, v, visited):
    visited[v] = True #방문하면 True
    print(v, end=' ')

    for i in g[v]: #시작노드와 연결된 노드 중에서
        if not visited[i]: #방문 안 한 노드가 있다면
            dfs(g,i, visited) #해당 노드부터 다시 탐색



def bfs(g, v, visited):
    q = deque([v]) #시작노드 큐에 삽입

    visited[v] = True #시작노드 방문

    while q:
        v = q.popleft() #시작노드 pop
        print(v, end=' ')
        for i in g[v]: #시작노드와 연결된 모든 노드 중에서
            if not visited[i]: #방문 안 한 노드가 있다면
                q.append(i) #큐에 넣고 
                visited[i] = True #방문
        #현재 노드와 연결된 모든 노드를 방문했으면 제일 먼저 방문한 노드 pop





qty, n, start = map(int, input().split())

#그래프, 방문 리스트 초기화
graph = [[] for _ in range(qty+1)]
visi = [False for _ in range(qty+1)]

#그래프에 노드 정보 입력
for _ in range(n):
    i, node = map(int, input().split())
    graph[i].append(node)
    graph[node].append(i)

#각 노드 오름차순으로 정렬
for i in range(qty+1):
    graph[i].sort()


dfs(graph, start, visi)
visi = [False for _ in range(qty+1)]
print()
bfs(graph, start, visi)
