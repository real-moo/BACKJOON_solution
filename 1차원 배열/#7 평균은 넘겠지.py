C = int(input())                        # 테스트 케이스의 개수

for i in range(C):
    grade_list = list(map(int, input().split()))
    avg = sum(grade_list[1:]) / grade_list[0]   # grade_list[0] = 학생의 수 / grade_list[1:] = 학생의 수를 제외한 점수
    count = 0
    for j in grade_list[1:]:            # 구한 평균과 학생의 점수를 비교
        if j > avg:
            count += 1
    rate = count / grade_list[0] * 100  # 평균이 넘는 학생의 비율 계산
    print ("%.3f"%rate+"%")
