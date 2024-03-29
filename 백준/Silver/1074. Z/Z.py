import sys

N, r, c = map(int, input().split())

ans = 0

# N이 0이 될 때까지 반복
while N != 0:
    N -= 1

    # (r, c)가 1사분면에 있는지 확인
    if r < 2**N and c < 2**N:
        # 첫 번째 사분면은 방문 순서에 추가되지 않으므로 ans 값 변동 없음
        ans += (2**N) * (2**N) * 0

    # (r, c)가 2사분면에 있는지 확인
    elif r < 2**N and c >= 2**N:
        # 두 번째 사분면까지의 방문 순서 계산
        ans += (2**N) * (2**N) * 1
        # 열 값을 줄여서 다음 반복에서는 1사분면으로 계산될 수 있게 함
        c -= 2**N

    # (r, c)가 3사분면에 있는지 확인
    elif r >= 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 2
        # 행 값을 줄여서 다음 반복에서는 1사분면으로 계산될 수 있게 함
        r -= 2**N

    # 나머지 경우는 4사분면에 있다고 판단
    else:
        ans += (2**N) * (2**N) * 3
        # 행,열 값 줄이기
        r -= 2**N
        c -= 2**N

print(ans)
