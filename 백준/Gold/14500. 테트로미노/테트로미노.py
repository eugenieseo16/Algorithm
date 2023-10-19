import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

max_ans = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# ㅗ 모양이 아닐때에는 dfs로 3전까지 방문한 후, 최대값 구하기
def dfs(x, y, cnt, total):
    global max_ans
    if cnt == 4:
        max_ans = max(max_ans, total)
        return
    else:
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, cnt+1, total+paper[nx][ny])
                visited[nx][ny] = 0


# ㅗ 모양일때는 중간기준으로 3개의 방향을 확인
def exce(x, y):
    global max_ans
    total = []
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            # 범위안에 있으면 배열에 넣고
            total.append(paper[nx][ny])
    # 배열의 크기가 3이상일때만 max값 구하고 비교
    if len(total) >= 3:
        total.sort(reverse=True)
        temp = sum(total[0:3]) + paper[x][y]

        max_ans = max(max_ans, temp)


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = 0

        exce(i, j)

print(max_ans)
