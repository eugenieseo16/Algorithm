T = int(input())

# 1은 (1) --> f(1) = 1
# 2는 (1,1),(2) --> f(2) = 2
# 3은 (1,1,1),(1,2),(2,1),(3) f(3) = 4
# 예시 속 4 : 1,3 2,2 3,1로 쪼개지니까
# 1에서 f(3)
# 2에서 f(2)
# 3에서 f(3) --> f(3) + f(2) + f(1)


def finding(N):
    global result
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        result = finding(N-1) + finding(N-2) + finding(N-3)
        return result

for _ in range(T):
    num = int(input())
    result = 0
    ans = finding(num)
    print(ans)

