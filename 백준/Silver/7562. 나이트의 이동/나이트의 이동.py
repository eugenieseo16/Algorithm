import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

# 폰의 이동 가능 범위
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(T):
    N = int(input())
    # 방문기록 표시
    board = [[0]*(N) for _ in range(N)]

    # 폰의 현 위치
    x, y = map(int, input().split())
    # 목적지
    tox, toy = map(int, input().split())

    queue = deque()
    queue.append((x, y))

    cnt = 0

    while queue:
        i, j = queue.popleft()

        #  목적지와 현위치가 같다면 반복뮨 탈출
        if i == tox and j == toy:
            cnt = board[i][j]
            break
        # 다르다면
        else:
            # 현 위치에서 갈수 있는 범위를 구한 후,
            for idx in range(8):
                ni = i + dx[idx]
                nj = j + dy[idx]
                #  보드 판 내 범위에 있고,
                if ni >= 0 and ni < N and nj >= 0 and nj < N:
                    # 방문한 적 없다면
                    if board[ni][nj] == 0:
                        # 큐에 넣고
                        queue.append((ni, nj))
                        # 이전 기록 + 1
                        board[ni][nj] = board[i][j] + 1
    print(cnt)
