import sys

input = sys.stdin.readline

L, C = map(int, input().split())
words = list(input().rstrip().split())
words.sort()

# 모음 리스트
vowel = ["a", "e", "i", "o", "u"]


# 생성된 암호가 조건에 맞는지 확인하는 함수
def checking(password):
    vw = 0
    cs = 0
    for pw in password:
        if pw in vowel:
            vw += 1
        else:
            cs += 1
    # 최소 1개의 모음과 2개의 자음이 있을 경우 출력
    if vw >= 1 and cs >= 2:
        print("".join(password))


def backtracking(arr):
    # 암호의 길이가 L이면 조건 확인 함수 호출
    if len(arr) == L:
        checking(arr)
        return
    else:
        for i in range(len(arr), C):
            # arr의 마지막 원소보다 큰 원소만 추가
            if arr[-1] < words[i]:
                arr.append(words[i])
                # 백트래킹을 위해 마지막 원소 제거
                backtracking(arr)
                arr.pop()


for idx in range(C - L + 1):
    arr = [words[idx]]
    backtracking(arr)
