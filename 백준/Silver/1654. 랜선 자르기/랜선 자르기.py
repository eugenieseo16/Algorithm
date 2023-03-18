

K, N = map(int, input().split())

arr = []
for _ in range(K):
    arr.append(int(input()))

start = 1
end = max(arr)

# 범위는 1부터, 가지고 있는 랜선의 길이 중 가장 긴 것
while (start <= end):
    mid = (start + end) // 2
    count = 0

    # 모든 랜선 값을 mid로 나누어 총 몇개의 랜선이 나오는지 확인
    for i in range(K):
        count += arr[i] // mid

    # 자른 갯수가 N 이상이면 mid+1을 start로 두고 다시 while문 반복
    if count >= N:
        start = mid + 1
    # 자른 갯수가 N 이하면 mid-1을 end로 두고 다시 while문 반복
    else:
        end = mid - 1
# 최대 랜선 길이를 구해야 하므로, end를 출력
print(end)