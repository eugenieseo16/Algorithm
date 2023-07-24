import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
prefix = [0]
sum_num = 0

for n in numbers:
    sum_num += n
    prefix.append(sum_num)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
