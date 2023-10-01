import sys
from collections import deque

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
snake = dict()
ladder = dict()

board = [0] * 101
visited = [0] * 101

# 사다리 정보 저장
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
# 뱀 정보 저장
for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y

Q = deque()
Q.append(1)
while Q:
    now = Q.popleft()
    # 100번 칸에 도착하면, 결과를 출력하고 종료한다.
    if now == 100:
        print(board[100])
        break
    else:
        # 주사위를 굴린 결과로 이동할 칸
        for i in range(1, 7):
            next = now + i
            # 이동한 칸이 게임판 내에 있고, 아직 방문하지 않았다면
            if next <= 100 and not visited[next]:
                # 이동한 칸에 사다리가 있다면, 사다리를 타고 이동한다.
                if next in ladder.keys():
                    next = ladder[next]
                # 이동한 칸에 뱀이 있다면, 뱀을 타고 이동한다.
                elif next in snake.keys():
                    next = snake[next]
                # 다시한번 검사 후, 방문 처리하고, 큐에 추가
                if not visited[next]:
                    visited[next] = 1
                    Q.append(next)
                    board[next] = board[now] + 1
