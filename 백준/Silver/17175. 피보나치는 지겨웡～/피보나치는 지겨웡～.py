N = int(input())

arr = [1,1]
if N < 2:
    print(arr[N])
else:
    for _ in range(N-1):
        arr.append(arr[-1] + arr[-2] + 1)
    print(arr[-1] % 1000000007)