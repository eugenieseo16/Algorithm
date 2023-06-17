N, K = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 0
counter = [0] * (max(numbers) + 1)
ans = 0
while end < N:
    if counter[numbers[end]] < K:
        counter[numbers[end]] += 1
        end += 1

    else:
        counter[numbers[start]] -= 1
        start +=1
    ans = max(ans , end-start)
print(ans)