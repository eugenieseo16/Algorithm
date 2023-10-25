import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]

w, h = map(int, input().split())
while w != 0 and h != 0:
    if w == 1 and h == 1:
        print(int(input()))
    else:
        terr = [list(map(int, input().split())) for _ in range(h)]
        visited = [[0]*w for _ in range(h)]
        queue = deque()
        cnt = 1
        for i in range(h):
            for j in range(w):
                if terr[i][j] == 1 and visited[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = cnt

                    while queue:
                        x, y = queue.popleft()
                        for idx in range(8):
                            nx = x + dx[idx]
                            ny = y + dy[idx]
                            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                                if visited[nx][ny] == 0 and terr[nx][ny] == 1:
                                    queue.append((nx, ny))
                                    visited[nx][ny] = cnt
                    cnt += 1
        print(cnt-1)
    w, h = map(int, input().split())
