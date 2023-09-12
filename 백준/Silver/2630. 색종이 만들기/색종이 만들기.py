import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0


def cutting(x, y, N):
    global blue, white
    color = paper[x][y]
    # 현재 종이에서 모든 칸이 같은 색인지 확인
    for i in range(x, x + N):
        for j in range(y, y + N):
            # 다른 색의 칸이 있다면 4등분하여 각 부분에 대해 재귀적으로 함수 호출
            if color != paper[i][j]:
                cutting(x, y, N // 2)
                cutting(x, (y + (N // 2)), N // 2)
                cutting((x + (N // 2)), y, N // 2)
                cutting((x + (N // 2)), (y + (N // 2)), N // 2)
                return
    # 모든 칸이 같은 색이면 해당 색의 카운터 증가
    if color == 0:
        white += 1
    else:
        blue += 1


cutting(0, 0, N)
print(white)
print(blue)
