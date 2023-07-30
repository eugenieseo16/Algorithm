import sys
from collections import defaultdict

x_list = defaultdict(int)
y_list = defaultdict(int)

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_list[x] += 1
    y_list[y] += 1
ans_x = [k for k, v in x_list.items() if v == 1]
ans_y = [k for k, v in y_list.items() if v == 1]

print(ans_x[0], ans_y[0])
