import sys

# sys.stdin = open("input.txt")

input = sys.stdin.readline
for _ in range(3):
    N = int(input())
    S = 0
    for _ in range(N):
        S += int(input())
    if S > 0:
        print("+")
    elif S == 0:
        print(0)
    else:
        print("-")