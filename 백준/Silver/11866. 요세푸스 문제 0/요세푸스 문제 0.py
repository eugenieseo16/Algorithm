import sys
from collections import deque

N, K = map(int,input().split())
circle = deque()
result = []


for num in range(1, N+1):
    circle.append(num)

while circle:
    for k in range(K-1):
        circle.append(circle.popleft())
    result.append(circle.popleft())


print("<", end='')
print(', '.join(map(str,result)), end='>')