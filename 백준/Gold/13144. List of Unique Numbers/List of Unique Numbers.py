# 시간초과로 인해 sliding window 사용

N = int(input())
arr = list(map(int, input().split()))
max_num = max(arr) + 1

check = [0] * max_num
count = 0
end = 0

for start in range(N):
    while end < N and check[arr[end]] == 0:
        check[arr[end]] = 1
        end += 1
        count += end - start

    check[arr[start]] = 0

print(count)
