import sys

N = int(input())

def rounding(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


if N == 0:
    print(0)
else:
    standard = rounding(N * 0.15)
    length = N - standard
    scores = [int(sys.stdin.readline()) for _ in range(N)]

    new_scores = sorted(scores)[standard:length]
    ans = rounding(sum(new_scores) / len(new_scores))
    print(ans)
