import sys

T = int(input())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    height = N % H
    weight = (N // H) + 1

    if height == 0:
        height = H
        weight -= 1

    ans = (height * 100) + weight
    print(ans)
