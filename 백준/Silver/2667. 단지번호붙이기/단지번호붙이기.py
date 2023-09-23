import sys
from collections import deque

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
queue = deque()
houses = list(input().rstrip() for _ in range(N))
visited = [[0] * (N) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
num_houses = []


def BFS():
    house = 1
    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if not visited[nx][ny] and houses[nx][ny] == "1":
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    house += 1

    num_houses.append(house)


count = 0

for i in range(N):
    for j in range(N):
        if houses[i][j] == "1" and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = 1
            BFS()
            count += 1
print(count)
num_houses.sort()
for num in num_houses:
    print(num)
