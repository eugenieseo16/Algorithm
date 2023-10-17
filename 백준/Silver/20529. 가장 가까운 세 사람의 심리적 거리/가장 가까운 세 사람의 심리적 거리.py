import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    mbtis = list(input().split())
    ans = 12

    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i == j or j == k or i == k:
                        continue
                    else:
                        temp = 0
                        for x in range(4):
                            if mbtis[i][x] != mbtis[j][x]:
                                temp += 1
                            if mbtis[k][x] != mbtis[j][x]:
                                temp += 1
                            if mbtis[i][x] != mbtis[k][x]:
                                temp += 1
                        if temp < ans:
                            ans = temp
        print(ans)
