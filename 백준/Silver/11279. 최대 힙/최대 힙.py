import sys
import heapq

# sys.stdin = open("input.txt")
input = sys.stdin.readline
numbers = []
N = int(input())
for _ in range(N):
    x = int(input())
    if not x:
        if numbers:
            num = heapq.heappop(numbers)
            print(-num)
        else:
            print(0)
    else:
        heapq.heappush(numbers, -x)
