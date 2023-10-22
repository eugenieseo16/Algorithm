import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
max_res = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(num):
    queue = deque()
    visited = list([0] * N for _ in range(N))
    # 안전구역의 수를 저장할 변수
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 침수 당하지 않았고, 방문한 적 없으면
            if area[i][j] - num > 0 and not visited[i][j]:
                # 큐에 저장하고, 안적구역 수  + 1
                queue.append((i, j))
                cnt += 1
                visited[i][j] = 1
                # 연결된 구역들 모두 방문 체크
                while queue:
                    x, y = queue.popleft()
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if nx >= 0 and nx < N and ny >= 0 and ny < N:
                            if not visited[nx][ny] and area[nx][ny] - num > 0:
                                queue.append((nx, ny))
                                visited[nx][ny] = 1
    #  최댓값 저장
    global max_res
    max_res = max(max_res, cnt)


rain = 0
for n in range(N):
    rain = max(rain, max(area[n]))

#  1부터 배열 내 최대숫자 -1 까지 늘려가며 최대 안전구역 수 계산
for i in range(1, rain+1):
    bfs(i)
print(max_res)
