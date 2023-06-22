
from collections import deque

M, N = map(int,input().split())
box = []
count = 0

box = [list(map(int, input().split())) for _ in range(N)]

tomato = deque([])
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while tomato:
    temp = tomato.popleft()
    for d in range(4):
        if temp[0] + dx[d] >= 0 and temp[0] + dx[d] < N and temp[1] + dy[d] >= 0 and temp[1] + dy[d] < M:
            if box[temp[0] + dx[d]][temp[1] + dy[d]] == 0:
                box[temp[0] + dx[d]][temp[1] + dy[d]] = box[temp[0]][temp[1]] + 1
                tomato.append([temp[0] + dx[d], temp[1] + dy[d]])
max_num = 0
for num in range(N):
    if 0 in box[num]:
        max_num = -1
        break
    if max(box[num]) > max_num and max_num != -1:
        max_num = max(box[num]) -1

print(max_num)


