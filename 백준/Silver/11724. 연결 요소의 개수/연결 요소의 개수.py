import sys

# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def DFS(tree, visited, node):
    visited[node] = 1
    for num in tree[node]:
        if not visited[num]:
            DFS(tree, visited, num)


N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

count = 0
for idx in range(1, N + 1):
    if not visited[idx]:
        DFS(tree, visited, idx)
        count += 1
print(count)
