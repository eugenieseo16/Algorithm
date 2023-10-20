import sys
input = sys.stdin.readline

N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    houses[i][0] = min(houses[i-1][1], houses[i-1][2]) + houses[i][0]
    houses[i][1] = min(houses[i-1][2], houses[i-1][0]) + houses[i][1]
    houses[i][2] = min(houses[i-1][1], houses[i-1][0]) + houses[i][2]

print(min(houses[N-1][0], houses[N-1][1], houses[N-1][2]))
