import sys
from collections import defaultdict

# sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cloth = defaultdict(int)
    N = int(input())
    for _ in range(N):
        name, cate = input().split()
        cloth[cate] += 1
    ans = 1
    for value in cloth.values():
        #     print(key, value)
        ans *= value + 1
    print(ans - 1)
