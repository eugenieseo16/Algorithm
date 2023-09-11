import sys

L = int(input())
arr = list(map(int, input().split()))
arr.sort()
N = int(input())

count = 0
# N이 집합에 속해있는 수라면 좋은집합 생성이 불가능
if N in arr:
    count = 0
# N이 집합안의 제일 작은 수 보다 작을 때
elif N < arr[0]:
    count += ((N - 1) * (arr[0] - N)) + (arr[0] - N - 1)
else:
    # N이 집한 안의 두 수 사이에 있을 때
    for i in range(1, L):
        if arr[i] > N and arr[i - 1] < N:
            count += ((N - arr[i - 1] - 1) * (arr[i] - N)) + (arr[i] - N - 1)
            break
print(count)
