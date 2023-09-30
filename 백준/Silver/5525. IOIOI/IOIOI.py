import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
P = "I" + (("OI") * N)
M = int(input())
S = input()

idx = 0
cnt = 0
ans = 0

while idx <= M - 2:
    if S[idx : idx + 3] == "IOI":
        cnt += 1
        idx += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        cnt = 0
        idx += 1
print(ans)
