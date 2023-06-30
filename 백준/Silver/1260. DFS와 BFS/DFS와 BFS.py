from collections import deque

N, M, V= map(int, input().split())
tree = list([] for _ in range(N+1)) # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    # 작은 수 부터 방문하기 위해 정렬
    tree[a].sort()
    tree[b].sort()

visited_DFS = [0] * (N+1)
visited_BFS = [0] * (N+1)

ans_DFS = []
ans_BFS = []

def DFS(tree,v,visited,ans):
    visited[v] = 1
    ans.append(v)

    for w in tree[v]:
        if visited[w] == 0:
            DFS(tree,w,visited,ans)

def BFS(tree,v,visited,ans):
    queue = deque([v])
    visited[v] = 1
    while queue:
        w =queue.popleft()
        ans.append(w)
        for x in tree[w]:
            if visited[x] == 0:
                queue.append(x)
                visited[x] = 1

DFS(tree,V,visited_DFS,ans_DFS)
BFS(tree,V,visited_BFS,ans_BFS)
print(*ans_DFS)
print(*ans_BFS)