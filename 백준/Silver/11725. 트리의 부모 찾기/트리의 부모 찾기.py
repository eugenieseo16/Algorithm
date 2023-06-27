import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

def dfs(start, tree_arr, parent_arr):
    for node in tree_arr[start]:
        if parent_arr[node] == 0 :
            parent_arr[node] = start
            dfs(node, tree_arr, parent_arr)

N = int(input())
tree = list([] for _ in range(N+1))
parents = list(0 for _ in range(N+1))
for n in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
parents[1] = -1
dfs(1,tree,parents)

for i in range(2, N+1):
    print(parents[i])

