numbers = list(map(int, input().split()))
numbers.sort()


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


ans = gcd(numbers[0], numbers[1])


def lcm(a, b):
    return (a * b) // ans


ans2 = lcm(numbers[0], numbers[1])
print(ans)
print(ans2)
