import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P = input().rstrip()
    N = int(input())
    arr = input().rstrip()

    # 빈 리스트를 입력받으면 빈 deque 생성
    if N == 0:
        new_arr = deque()
    # 받은 인풋에서 괄호 제외 후, 쉼표로 분리하고, int로 변경해서 deque 생성
    else:
        new_arr = deque(map(int, arr.strip("[]").split(",")))

    # 뒤집힌 경우 true로 변환
    reverse = False
    # error 출력 용 flag
    flag = 1

    for func in P:
        # 함수가 R이면 뒤집힘 표시 반전
        if func == "R":
            reverse = not (reverse)
        else:
            if new_arr:
                # 뒤집혀있다면 오른쪽에서 pop
                if reverse == True:
                    new_arr.pop()
                # 안 뒤집혀있다면 왼쪽에서 pop
                else:
                    new_arr.popleft()
            else:
                flag = 0
                print("error")
                break

    # 함수 실행도중 에러가 안났다면
    if flag:
        ans = list(new_arr)
        # 뒤집혔는지 확인 후 , 츨력
        if reverse == True:
            ans = ans[::-1]
        # print(ans)를 했더니 리스트 형식이라 오답처리됨
        print("[" + ",".join(map(str, ans)) + "]")
