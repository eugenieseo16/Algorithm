N, M = map(int, input().split())
basket = [0 for _ in range(N)]

for _ in range(M):
    i,j,k = map(int, input().split())
    for x in range(i,j+1):
        basket[x-1] = k

for n in range(N):
    print(basket[n], end = ' ')