import sys
#sys.stdin = open('18352.txt')
#시간초과가 뜰 수도 있을 것 같은데 BFS로 풀어봄
from collections import deque

# 첫째 줄에 도시의 개수 N (2 ≤ N ≤ 300,000)
# 도로의 개수 M (1 ≤ M ≤ 1,000,000)
# 거리 정보 K (1 ≤ K ≤ 300,000)
# 출발 도시의 번호 X (1 ≤ X ≤ N)
N, M, K, X = map(int, sys.stdin.readline().split())

# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.
# 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다.
# (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

#도로정보를 담을 리스트
road = [[] for _ in range(N+1)]

#방문기록 리스트
visited = [0] * (N+1)

#시작을 1로 지정(나중에 K+1!)
visited[X] = 1

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    road[A].append(B)

Q = deque()
Q.append(X)

while Q:
    i = Q.popleft()
    # 방문하면 이전기록 + 1
    for j in road[i]:
        if visited[j] == 0:
            visited[j] = visited[i] + 1
            Q.append(j)

# 방문기록에서 찾아야하는 수가 있다면 인덱스번호 프린트
if K+1 in visited:
    for k in range(1, N + 1):
        # 시작을 1로 지정해서 K에 1을 더해줘야한다.
        if visited[k] == K+1:
            print(k)
# 없으면 -1 프린트
else:
    print(-1)