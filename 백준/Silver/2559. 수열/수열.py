N, K = map(int, input().split())
numbers = list(map(int, input().split()))

acc_sum = sum(numbers[:K])
max_sum = acc_sum
for i in range(N - K):
    acc_sum = acc_sum - numbers[i] + numbers[i + K]
    if acc_sum > max_sum:
        max_sum = acc_sum
print(max_sum)
