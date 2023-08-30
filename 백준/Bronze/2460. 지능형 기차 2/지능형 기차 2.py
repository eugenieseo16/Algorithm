import sys

input = sys.stdin.readline
stations = [[0, 0]]
for _ in range(10):
    x, y = map(int, input().split())
    stations.append([x, y])

max_people = stations[1][1]
people = stations[1][1]
num = 1
for i in range(2, 11):
    people = people - stations[i][0] + stations[i][1]
    if people > max_people:
        max_people = people
        num = i
print(max_people)
