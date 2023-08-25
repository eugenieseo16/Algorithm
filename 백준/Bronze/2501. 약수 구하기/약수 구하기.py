N, K = map(int, input().split())
numbers = [0]
for i in range(1, N + 1):
    if N % i == 0:
        numbers.append(i)
if len(numbers) - 1 < K:
    print(0)
else:
    print(numbers[K])
