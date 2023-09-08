import sys

N = int(input())
numbers = list(map(int, input().split()))
new_nums = []

# 원래의 인덱스를 함께 저장
for i in range(N):
    new_nums.append([i, numbers[i]])

# 좌표 값을 기준 오름차순 정렬
new_nums = sorted(new_nums, key=lambda x: x[1])
# 동일한 좌표 값의 갯수를 세는 변수
count = 0
for idx in range(N):
    if idx == 0:
        new_nums[idx].append(idx)
    else:
        # 이전 좌표 값과 동일한 경우
        if new_nums[idx][1] == new_nums[idx - 1][1]:
            count += 1
            new_nums[idx].append(new_nums[idx - 1][2])
        # 다른 경우 새로운 좌표 값 할당
        else:
            new_nums[idx].append(idx - count)

# 원래 순서로 다시 정렬
new_nums = sorted(new_nums, key=lambda x: x[0])
for j in range(N):
    print(new_nums[j][2], end=" ")
