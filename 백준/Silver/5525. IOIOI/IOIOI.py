import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
P = "I" + (("OI") * N)
M = int(input())
S = input()
idx = 0
cnt = 0
L = len(P)
while idx <= M - L:
    if S[idx : idx + L] == P:
        cnt += 1
    idx += 1
print(cnt)
