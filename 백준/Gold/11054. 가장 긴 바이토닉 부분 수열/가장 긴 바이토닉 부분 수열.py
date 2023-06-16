N = int(input())
arr = list(map(int, input().split()))
arr_rev = arr[::-1]

increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]

for i in range(1,N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if arr_rev[i] > arr_rev[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

answer = [-1 for _ in range(N)]
for n in range(N):
    answer[n] += (increase[n] + decrease[N-n-1])
print(max(answer))