import sys
from collections import deque, defaultdict

# 보드, 방문기록 dict 만들기
N, M, A, B, K = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(M)] for _ in range(N)]
visited = defaultdict(int)

# 장애물 위치 설정
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x - 1][y - 1] = 1

# 시작 위치와 끝 위치 설정
start = list(map(int, sys.stdin.readline().split()))
end = list(map(int, sys.stdin.readline().split()))
start[0] -= 1
start[1] -= 1
end[0] -= 1
end[1] -= 1


# 보드 안에 있는 지 체크
def is_in_board(new_x, new_y):
    # 꼭지검 4개 전부 확인
    # 왼쪽 위
    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
        return False
    # 오른쪽 위
    if new_x + (A - 1) < 0 or new_x + (A - 1) >= N or new_y < 0 or new_y >= M:
        return False
    # 왼쪽 아래
    if new_x < 0 or new_x >= N or new_y + (B - 1) < 0 or new_y + (B - 1) >= M:
        return False
    # 오른쪽 아래
    if (
        new_x + (A - 1) < 0
        or new_x + (A - 1) >= N
        or new_y + (B - 1) < 0
        or new_y + (B - 1) >= M
    ):
        return False
    #  다 범위안에 있다면
    return True


#  장애물 없는지 확인
def is_no_barrier(new_x, new_y):
    for i in range(new_x, new_x + A):
        for j in range(new_y, new_y + B):
            if board[i][j] == 1:
                return False
    return True


Q = deque()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# 시작 지점 추가
Q.append((start, 0))
visited[(start[0], start[1])] = 1

while Q:
    position, cnt = Q.popleft()
    # 끝을 만나면 탈출
    if position[0] == end[0] and position[1] == end[1]:
        print(cnt)
        break
    for d in range(4):
        new_x = position[0] + dx[d]
        new_y = position[1] + dy[d]
        if is_in_board(new_x, new_y):
            if is_no_barrier(new_x, new_y):
                if visited[(new_x, new_y)] == 0:
                    visited[(new_x, new_y)] = 1
                    Q.append(([new_x, new_y], cnt + 1))
else:
    print(-1)
