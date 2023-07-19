N = int(input())

arr = list(map(int, input().split()))
X = int(input())
ans = []


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


for number in arr:
    if number != X and gcd(number, X) == 1:
        ans.append(number)

print(sum(ans) / len(ans))
