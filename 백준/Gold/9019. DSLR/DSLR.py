import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline

# D 함수: n * 2 를 10000으로 나눈 나머지를 반환


def D(n):
    return (n * 2) % 10000

# S 함수: n 값에서 1을 빼는 함수. n이 0이면 9999를 반환


def S(n):
    if n == 0:
        n = 9999
    else:
        n -= 1
    return n


# L 함수: n 값을 왼쪽으로 한 칸 씩 밀기
def L(n):
    return (n // 1000) + ((n % 1000) * 10)

# R 함수: n 값을 오른쪽으로 한 칸 씩 밀기


def R(n):
    return (n // 10) + ((n % 10) * 1000)


T = int(input())
for _ in range(T):

    now, target = map(int, input().split())
    visited = [0] * 10001

    queue = deque()
    queue.append((now, ''))
    visited[now] = 1

    while queue:
        temp_n, way = queue.popleft()
        if temp_n == target:
            print(way)
            break

        d = D(temp_n)
        if not visited[d]:
            visited[d] = 1
            queue.append((d, way + 'D'))
        s = S(temp_n)
        if not visited[s]:
            visited[s] = 1
            queue.append((s, way + 'S'))
        l = L(temp_n)
        if not visited[l]:
            visited[l] = 1
        queue.append((l, way + 'L'))
        r = R(temp_n)
        if not visited[r]:
            visited[r] = 1
            queue.append((r, way + 'R'))
