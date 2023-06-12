# 유니온 파인드는 그래프 알고리즘으로 두 노드가 같은 집합에 속하는지 판별하는 알고리즘입니다.
# 두 노드를 합쳐 하나의 집합을 만드는 Union연산과
# 자신의 루트 노드를 찾는 Find연산으로 이루어진다.

import sys
sys.setrecursionlimit(100000)
N, M = map(int, sys.stdin.readline().split())

# 부모를 담을 배열( 초기 값은 자기 자신이 부모)
parent = [i for i in range(N+1)] # 예제의 경우: [1,2,3,4,5,6,7]

# 파인드 함수 정의
def find(a):
    # a의 부모가 a라면, a를 리턴
    if a == parent[a]:
        return a
    # 아니라면 계속해서 부모를 찾기위해 올라간다.
    parent[a] = find(parent[a])
    return parent[a]


# 유니온 함수 정의
def union(a,b):
    # 1. 부모를 찾음
    parent_a = find(a)
    parent_b = find(b)
    # 2. a의 부모를 b의 부모로 기록
    parent[parent_a] = parent_b

answers = []

for _ in range(M):
    Q, a, b = map(int, sys.stdin.readline().split())
    #  만약 Q가 0이면, Union을 실행.
    if Q == 0 :
        union(a,b)
    # 1이면 Find를 실행
    else:
        # a와 b의 최종 부모가 같다면,
        if find(a) == find(b):
            answers.append("YES")
        else:
            answers.append("NO")

print("\n".join(answers))