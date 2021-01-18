T = int(input())    # 테스트 케이스 입력

for i in range(T):
    num = input()	# 문자열 입력
    score = 0		# 점수를 0으로 초기화
    s_sum = 0		# 점수를 합하기 위한 변수를 0으로 초기화
    for j in num:
        if j == 'O':
            score += 1
        else:
            score = 0
        s_sum += score
    print(s_sum)
