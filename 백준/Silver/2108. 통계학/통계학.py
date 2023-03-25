import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
#평균
ave = int(round(sum(arr)/N, 0))

#중앙
sor_arr = sorted(arr)
med = sor_arr[(N//2)]

#범위
ran = sor_arr[-1] - sor_arr[0]

#최빈값
mode_dict = {}


for j in arr:
    if mode_dict.get(j) is None:
        mode_dict[j] = 1
    else:
        mode_dict[j] += 1
max_num = max(mode_dict.values())
max_list = []

for k,v in mode_dict.items():
    if v == max_num:
        max_list.append(k)

if len(max_list) == 1:
    mode = max_list[0]
else:
    mode = sorted(max_list)[1]


print(ave)
print(med)
print(mode)
print(ran)