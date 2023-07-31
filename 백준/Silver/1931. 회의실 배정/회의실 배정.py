import sys

T = int(input())
time = []
for _ in range(T):
    start, end = map(int, sys.stdin.readline().split())
    time.append([start, end])
time.sort(key=lambda x: (x[1], x[0]))

now = 0
ans = 0
for t in time:
    if now <= t[0]:
        ans += 1
        now = t[1]

print(ans)
