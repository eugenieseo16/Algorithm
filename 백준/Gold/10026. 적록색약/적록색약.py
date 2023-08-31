import sys
import copy

input = sys.stdin.readline

N = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS_color(x, y):
    color = picture[x][y]
    queue_color = [(x, y)]
    while queue_color:
        x, y = queue_color.pop()
        picture[x][y] = "0"
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if picture[nx][ny] == color:
                    queue_color.append((nx, ny))


def DFS(x, y):
    color = visited[x][y]
    queue = [(x, y)]

    while queue:
        x, y = queue.pop()
        visited[x][y] = "0"

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if color == "B":
                    if visited[nx][ny] == "B":
                        queue.append((nx, ny))
                else:
                    if visited[nx][ny] == "R" or visited[nx][ny] == "G":
                        queue.append((nx, ny))


picture = []
for _ in range(N):
    picture.append(list(input().rstrip()))

visited = copy.deepcopy(picture)
num_color = 0
num = 0

for i in range(N):
    for j in range(N):
        if picture[i][j] != "0":
            DFS_color(i, j)
            num_color += 1

        if visited[i][j] != "0":
            DFS(i, j)
            num += 1
print(num_color, num)
