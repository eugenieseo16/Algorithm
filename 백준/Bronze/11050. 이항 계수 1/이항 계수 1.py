N, K = map(int, input().split())

def solving(N, K):
    son = 1
    mom = 1
    if N == K:
        return 1
    else:
        K = min(K, N - K)
        for k in range(K):
            son *= N - k
            mom *= k + 1
    return son // mom


print(solving(N, K))
