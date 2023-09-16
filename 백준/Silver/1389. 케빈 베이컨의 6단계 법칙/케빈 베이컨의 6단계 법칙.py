import sys
from collections import deque

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        nodes = queue.popleft()
        # 현재 노드와 연결된 노드들을 순회
        for node in friends[nodes]:
            # 방문하지 않았다면 거리 정보 업데이트하고 큐에 추가
            if not visited[node]:
                visited[node] = visited[nodes] + 1
                queue.append(node)


N, M = map(int, input().split())
friends = [[] for _ in range(N + 1)]
# 최소 케빈 베이컨 수를 저장할 변수
connect = 500000
# 최소 케빈 베이컨 수를 가진 유저 번호를 저장할 변수
ans = 0

for _ in range(M):
    a, b = map(int, input().split())
    # a의 친구 리스트에 b를,
    friends[a].append(b)
    # b의 친구 리스트에 a를 추가
    friends[b].append(a)

for i in range(1, N + 1):
    # 각 노드까지의 거리를 저장할 리스트
    visited = [0] * (N + 1)
    BFS(i)
    # print(i, visited, sum(visited))
    # 만약 현재 유저의 케빈 베이컨 수가 이전 최소보다 작다면 업데이트
    if sum(visited) < connect:
        connect = sum(visited)
        ans = i
print(ans)
