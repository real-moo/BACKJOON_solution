N = int(input())
grade_list = list(map(int, input().split()))

h_grade = max(grade_list)

for i in range(N):
    grade_list[i] = grade_list[i] / h_grade * 100

avg = sum(grade_list) / N
print(avg)
