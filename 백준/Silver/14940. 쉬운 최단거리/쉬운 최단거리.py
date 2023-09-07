import sys
from collections import deque


input = sys.stdin.readline
N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

# BFS를 위한 큐 초기화
Q = deque()

# 모든 거리를 -1로 설정한 배열 생성
ans = [[-1] * M for _ in range(N)]

# 방문 여부를 체크
visited = [[0] * M for _ in range(N)]

# 지도 전체를 순회하며:
# 2를 찾아 BFS 큐에 추가하고, 0은 ans에 0으로 기록
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            Q.append((i, j))
            visited[i][j] = 1
            ans[i][j] = 0
        if maps[i][j] == 0:
            ans[i][j] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS 실행
while Q:
    x, y = Q.popleft()
    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]
        # 새로운 좌표가 지도 내에 있는지 확인
        if 0 <= nx < N and 0 <= ny < M:
            # 갈 수 있는 땅이며 아직 방문하지 않았다면 큐에 추가
            if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                Q.append((nx, ny))
                # 방문 표시
                visited[nx][ny] = 1
                # 거리 업데이트
                ans[nx][ny] = ans[x][y] + 1

# 결과 출력
for a in ans:
    print(*a)
