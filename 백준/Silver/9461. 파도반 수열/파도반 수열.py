import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    P = [0, 1, 1, 1]
    num = int(input())
    if num > 3:
        for i in range(4, num + 1):
            P.append(P[i - 3] + P[i - 2])
    print(P[num])
