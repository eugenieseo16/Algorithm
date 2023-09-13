import sys
import heapq

input = sys.stdin.readline

numbers = []
N = int(input())

for _ in range(N):
    n = int(input())
    if n == 0:
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print(0)
    else:
        heapq.heappush(numbers, n)
