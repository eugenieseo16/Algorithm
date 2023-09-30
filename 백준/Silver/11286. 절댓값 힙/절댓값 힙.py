import sys
import heapq
from collections import defaultdict

# sys.stdin = open("input.txt")
input = sys.stdin.readline

numbers = []
num_of_numbers = defaultdict(int)
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        if numbers:
            temp = heapq.heappop(numbers)
            if num_of_numbers[-temp] != 0:
                print(-temp)
                num_of_numbers[-temp] -= 1
            else:
                print(temp)
                num_of_numbers[temp] = -1
        else:
            print(0)
    else:
        if num > 0:
            heapq.heappush(numbers, num)
            num_of_numbers[num] += 1
        else:
            heapq.heappush(numbers, -num)
            num_of_numbers[num] += 1

