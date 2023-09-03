import sys

input = sys.stdin.readline

# 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)
N = int(input())
# 고장난 버튼의 개수 M (0 ≤ M ≤ 10)
M = int(input())
# 고장난 버튼
if M:
    broken = list(input().split())
else:
    broken = []
# 채널 100번 기준 최대값으로 최소를 설정
min_count = abs(100 - N)

# N은 최대 500000이지만, 위에서 올라올수도 있고, 아래에서 내려갈수도 있기 때문에 범위는 1000000
for num in range(1000001):
    num = str(num)
    len_num = len(num)
    # num의 숫자 하나하나 확인하면서
    for idx in range(len_num):
        # 고장난 숫자가 있다면 break
        if num[idx] in broken:
            break
        # 고장난 숫자 없다면, min_count와 비교
        elif idx == len_num - 1:
            min_count = min(min_count, abs(int(num) - N) + len_num)
print(min_count)
