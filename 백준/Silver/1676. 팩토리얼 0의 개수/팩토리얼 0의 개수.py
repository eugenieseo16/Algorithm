N = int(input())
import math

# def factorial(N):
#     if N > 1:
#         return N * factorial(N - 1)
#     else:
#         return 1


def solve(num):
    cnt = 0
    if num % 10 == 0:
        while num % 10 == 0:
            num //= 10
            cnt += 1
        return cnt
    else:
        return cnt


print(solve(math.factorial(N)))
