import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = list([0] * (N) for _ in range(N))


def bfs(i):
    q = deque()
    q.append(i)
    check = [0 for _ in range(N)]

    while q:
        num = q.popleft()

        for j in range(N):
            if check[j] == 0 and graph[num][j] == 1:
                q.append(j)
                check[j] = 1
                visited[i][j] = 1

for x in range(N):
    bfs(x)

for v in visited:
    print(*v)
