import sys
from collections import defaultdict

N = int(input())
N_numbers = list(map(int, input().split()))
M = int(input())
M_numbers = list(map(int, input().split()))

count = defaultdict(int)
ans = []
for i in range(N):
    count[N_numbers[i]] += 1
for j in range(M):
    ans.append(count[M_numbers[j]])

print(*ans)
