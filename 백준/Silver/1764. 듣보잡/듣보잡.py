import sys

input = sys.stdin.readline

N, M = map(int, input().split())
never_saw = []
never_heard = []
for _ in range(N):
    never_saw.append(input().rstrip())
for _ in range(M):
    never_heard.append(input().rstrip())

ans = sorted(list(set(never_saw) & set(never_heard)))
num = len(ans)
print(num)
for i in range(num):
    print(ans[i])
