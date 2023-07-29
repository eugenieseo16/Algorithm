import sys

grade_list = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
sum_grade = 0
sum_score = 0

for _ in range(20):
    name, score, grade = sys.stdin.readline().split()
    if grade != "P":
        sum_grade += grade_list[grade] * float(score)
        sum_score += float(score)

ans = sum_grade / sum_score
print(f"{ans:.6f}")
