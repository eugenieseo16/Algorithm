N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

for n in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = 1

ans = 0
for p in paper:
    ans += sum(p)
print(ans)