import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
campus = [input().rstrip() for _ in range(N)]
queue = deque()
visited = [[0] * (M) for _ in range(N)]
for n in range(N):
    for m in range(M):
        if campus[n][m] == "I":
            queue.append((n, m))
            visited[n][m] = 1
            break

ppl = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if not visited[nx][ny] and campus[nx][ny] != "X":
                queue.append((nx, ny))
                visited[nx][ny] = 1
                if campus[nx][ny] == "P":
                    ppl += 1
if ppl == 0:
    print("TT")
else:
    print(ppl)
