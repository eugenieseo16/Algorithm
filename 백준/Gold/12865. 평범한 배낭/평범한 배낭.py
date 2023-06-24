N , K = map(int, input().split())
items = [[0,0]]
temp_sum = [[0] * (K+1) for _ in range(N+1)]
for _ in range(N):
    items.append(list(map(int, input().split())))

for i in range(1,N+1):
    for j in range(1, K+1):
        W, V = items[i][0],items[i][1]
        if j < W :
            temp_sum[i][j] =  temp_sum[i-1][j]
        else:
            temp_sum[i][j] = max(temp_sum[i-1][j], V+temp_sum[i-1][j-W])

print(temp_sum[N][K])
