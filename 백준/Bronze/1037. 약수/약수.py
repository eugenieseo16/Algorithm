N = int(input())
if N == 1:
    num = int(input())
    print(num**2)
else:
    num = list(map(int,input().split()))
    min_num = min(num)
    max_num = max(num)
    print(min_num * max_num)