import sys
input = sys.stdin.readline

def find(a):
    # a의 부모가 a가 아니라면,
    if a != parents[a]:
        # 부모를 바꾸고
        parents[a] = find(parents[a])
    # 부모를 출력
    return parents[a]

def union(a,b):
    # 부모를 찾고,
    parent_a = find(a)
    parent_b = find(b)
    # 하나의 집합으로 만들기위해, 더 작은 수를 부모로 한다.
    if parent_a < parent_b :
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b
        

N = int(input())
M = int(input())

parents = [i for i in range(N)]

for i in range(N):
    connect = list(map(int,input().split())) 
    for j in range(N):
        if connect[j] == 1:
            union(i,j)

arr = [-1] + parents # [-1, 0, 0, 0]
journey = list(map(int, input().split()))
start = arr[journey[0]]
for x in range(1,M):
    if arr[journey[x]] != start:
        print("NO")
        break
else:
    print("YES")
