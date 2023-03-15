# ACM Craft : 건물을 짓기위해 필요한 최소 시간 구하기

# 위상정렬 알고리즘 & DP
# 부모 노드X인 노드를 queue에 넣는다.
# queue에서 원소를 하나씩 빼면서, 해당 노드로부터 갈 수 있는 모든 노드들에 대한 연결을 제거한다.
# 반복

import sys

from collections import deque

# 첫째 줄에는 테스트케이스의 개수 T가 주어진다.
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    # 건물의 개수 N과 건설순서 규칙 개수 K
    N, K = map(int, sys.stdin.readline().rstrip().split())
    # 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN이 공백을 사이로 주어진다.
    # [10, 1, 100, 10]
    rules = list(map(int, sys.stdin.readline().rstrip().split()))
    graph = [[] for _ in range(N + 1)]
    # 부모의 개수 저장 리스트
    parent_num = [0 for _ in range(N + 1)]
    # 최댓값 저장 할 리스트
    max_time = [0 for _ in range(N + 1)]
    Q = deque()

    # 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다.
    for k in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        # 그래프_부모의 인덱스[자식]
        # [[],[2,3],[4],[4],[]]
        graph[X].append(Y)
        # [[0],[0],[1],[1],[2]]
        parent_num[Y] += 1

    # 최종적으로 건설해야 할 건물의 번호 W가 주어진다.
    W = int(sys.stdin.readline().rstrip())

    for i in range(1, N + 1):
        # 만약에 부모가 없다면 Q에 추가
        if parent_num[i] == 0:
            Q.append(i)
            # 1번을 짓는데 걸리는 최대시간은 rules의 인덱스 0번 [10, 1, 100, 10] 즉, 10초
            # 최대시간을 기록
            max_time[i] = rules[i - 1]

    while Q:
        node = Q.popleft()
        # 그래프 : [[],[2,3],[4],[4],[]]
        for j in graph[node]:
            # 1번을 부모로 가진 애들의 부모 갯수를 하나씩 줄여줌
            parent_num[j] -= 1
            # 최대시간을 기록( 4번을 짓는데 걸리는 시간-> 이미 기록되어 시간, 지금계산한 시간 중 최대
            # 지금계산한 시간-> 부모 노드의 최대시간 + 현재 번호를 짓는데 걸리는 시간
            max_time[j] = max(max_time[j], max_time[node] + rules[j -1])
            # 다시 반복
            # 부모가 없다면 Q에 추가
            if parent_num[j] == 0:
                Q.append(j)

    print(max_time[W])