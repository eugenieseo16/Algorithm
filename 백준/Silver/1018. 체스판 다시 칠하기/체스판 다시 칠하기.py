import sys

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(sys.stdin.readline().rstrip())
count = []
#  8x8 로 자르기
for i in range(N - 7):
    for j in range(M - 7):
        #  흰색으로 시작 할 떄의 변화 기록
        w = 0
        #  검은색으로 시작 할 떄의 변화 기록
        b = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] == "W":
                        w += 1
                    else:
                        b += 1
                else:
                    if board[x][y] == "B":
                        w += 1
                    else:
                        b += 1
        count.append(w)
        count.append(b)
print(min(count))
