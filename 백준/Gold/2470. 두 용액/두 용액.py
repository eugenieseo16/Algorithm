# 2470
# 두 용액


N = int(input())
liquid = list(map(int, input().split()))

#  합이 0에 가장 가까운 용액 쌍을 찾기 쉽도록 정렬
liquid.sort()

start = 0
end = N-1

temp_ans = abs(liquid[start] + liquid[end])
ans = [liquid[start],liquid[end]]

while start < end :
    left = liquid[start]
    right = liquid[end]
    temp_sum = left + right


    if abs(temp_sum) < temp_ans:
        ans = [left, right]
        temp_ans = abs(temp_sum)
        if temp_sum == 0:
            break

    if temp_sum < 0 :
        start += 1
    else:
        end -= 1
print(ans[0], ans[1])

    