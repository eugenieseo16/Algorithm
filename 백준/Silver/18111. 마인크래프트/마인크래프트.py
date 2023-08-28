import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
idx = 0

for num in range(257):
    plus = 0
    minus = 0
    
    for i in range(N):
        for j in range(M):
            
            if blocks[i][j] > num:
                minus += blocks[i][j] - num
            else:
                plus += num - blocks[i][j]
    
    if B + minus >= plus:
        if plus + (minus * 2) <= ans:
            ans = plus + (minus * 2)
            idx = num

print(ans, idx)