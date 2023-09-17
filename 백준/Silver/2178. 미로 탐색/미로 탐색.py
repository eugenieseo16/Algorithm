import sys
from collections import deque

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def BFS():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if not visited[nx][ny] and miro[nx][ny] == "1":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


N, M = map(int, input().split())
miro = [input().rstrip() for _ in range(N)]
visited = [[0] * (M) for _ in range(N)]
queue = deque()
queue.append((0, 0))
visited[0][0] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

BFS()
print(visited[N - 1][M - 1])
