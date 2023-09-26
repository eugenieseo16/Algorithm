import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

s, e = 0, trees[-1]

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    if cnt >= M:
        s = mid + 1

    else:
        e = mid - 1
print(e)
