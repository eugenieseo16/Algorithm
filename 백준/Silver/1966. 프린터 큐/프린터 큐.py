from collections import defaultdict, deque
import sys

T = int(input())
for t in range(T):
    num, ans_idx = map(int, sys.stdin.readline().split())
    documents = deque()
    importances = list(map(int, sys.stdin.readline().split()))
    importances_dict = defaultdict(int)
    order = []
    # 순서와 중요도 기록
    for i in range(num):
        documents.append((i, importances[i]))
        importances_dict[importances[i]] += 1
    for j in range(9, 0, -1):
        while importances_dict[j] != 0:
            x, y = documents.popleft()
            if y == j:
                order.append(x)
                importances_dict[j] -= 1
            else:
                documents.append((x, y))
    print(order.index(ans_idx) + 1)
