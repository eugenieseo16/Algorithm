import sys
from collections import deque

N, K = map(int, input().split())
dist = [0] * 100001

def BFS():
    Q = deque()
    Q.append(N)
    while Q:
        x = Q.popleft()
        if x == K:
            print(dist[x])
            break
        else:
            for y in (x - 1, x + 1, x * 2):
                #  아직 값이 저장되지 않았고, 범위 안에 있는 값이라면 지금까지의 횟수 + 1로 저장
                if y >= 0 and y <= 100000 and dist[y] == 0:
                    dist[y] = dist[x] + 1
                    Q.append(y)
                    
BFS()
