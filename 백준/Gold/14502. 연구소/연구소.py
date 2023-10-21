import sys
import copy
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
result = 0

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 3개씩 모든 0에 벽을 세우고 최소 값을 계산
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    wall(cnt + 1)
                    lab[i][j] = 0


# 벽을 세운 상태에서 바이러스가 얼마나 퍼지는지 계산
def bfs():
    global result

    temp_arr = copy.deepcopy(lab)
    temp_q = copy.deepcopy(queue)

    while temp_q:
        x, y = temp_q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if temp_arr[nx][ny] == 0:
                    temp_arr[nx][ny] = 2
                    temp_q.append((nx, ny))
    temp_res = 0
    for i in range(N):
        temp_res += temp_arr[i].count(0)
    result = max(temp_res, result)


# 바이러스 위치 기억
queue = deque()
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            queue.append((i, j))

wall(0)
print(result)
