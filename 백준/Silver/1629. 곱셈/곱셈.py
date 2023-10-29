A, B, C = map(int, input().split())


def multiply(a, b):
    if b == 1:
        return a % C
    else:
        temp = multiply(a, b//2)
        if b % 2 == 0:
            return (temp ** 2) % C
        else:
            return (temp ** 2) * a % C


ans = multiply(A, B)
print(ans)
