import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

name, age, weight = input().split()
age, weight = int(age), int(weight)
while name != "#" and age and weight:
    if age > 17 or weight >= 80:
        team = "Senior"
        print(name, team)
    else:
        team = "Junior"
        print(name, team)
    name, age, weight = input().split()
    age, weight = int(age), int(weight)
