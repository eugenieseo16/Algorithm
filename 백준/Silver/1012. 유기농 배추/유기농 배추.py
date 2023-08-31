import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y):
    queue = [(x, y)]
    
    while queue:
        x, y = queue.pop()
        field[x][y] = 0
        
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if field[nx][ny] == 1:
                    queue.append((nx, ny))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    num = 0

    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                DFS(i, j)
                num += 1

    print(num)
