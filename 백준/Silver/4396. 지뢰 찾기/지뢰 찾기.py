# import sys
# sys.stdin = open('input.txt')


N = int(input())
bomb = [list(input()) for _ in range(N)]
board = [list(input()) for _ in range(N)]

dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [-1, 1, -1, 1, -0, 0, 1, -1]
bomb_xy = []

# 숫자라면 +1을, 숫자가 아니라면 1을 반환하도록 하는 함수


def add1(value):
    if isinstance(value, int):
        return value+1
    else:
        return 1


for i in range(N):
    for j in range(N):
        if bomb[i][j] == '*':
            bomb_xy.append((i, j))
            for idx in range(8):
                ni = i + dx[idx]
                nj = j + dy[idx]
                if ni < N and ni >= 0 and nj < N and nj >= 0:
                    if bomb[ni][nj] != '*':
                        bomb[ni][nj] = add1(bomb[ni][nj])


for x in range(N):
    for y in range(N):
        if board[x][y] == 'x':
            if bomb[x][y] == '*':
                for i, j in bomb_xy:
                    board[i][j] = '*'
            elif bomb[x][y] == '.':
                board[x][y] = '0'
            else:
                board[x][y] = str(bomb[x][y])


for b in board:
    print("".join(b))
