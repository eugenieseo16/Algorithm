import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

boxs = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# 방문기록
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

queue = deque()
ans = 0

# 방향
dx = [0, 0, 0, 0, -1, 1]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 1, -1, 0, 0]

# 토마토가 있다면(1이라면 큐에 넣기)
for a in range(H):
    for b in range(N):
        for c in range(M):
            if boxs[a][b][c] == 1:
                queue.append((a, b, c))
                visited[a][b][c] = 1


# bfs
def bfs():
    while queue:
        x, y, z = queue.popleft()
        for d in range(6):
            nx, ny, nz = x + dx[d], y + dy[d], z + dz[d]
            #  범위안에 있고,
            if nx >= 0 and nx < H and ny >= 0 and ny < N and nz >= 0 and nz < M:
                # 방문하지 않은 토마토가 들어있는(0) 곳이면
                if visited[nx][ny][nz] == 0 and boxs[nx][ny][nz] == 0:
                    #  이전 것  + 1 로 기록하고, 방문기록 체크
                    boxs[nx][ny][nz] = boxs[x][y][z] + 1
                    queue.append((nx, ny, nz))
                    visited[nx][ny][nz] = 1


bfs()

for a in range(H):
    for b in range(N):
        for c in range(M):
            # 안 익은 토마토가 있다면 -1 출력하고 모든 반복문 탈출
            if boxs[a][b][c] == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(boxs[a][b]))
print(ans - 1)
