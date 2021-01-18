N = num = int(input())
count = 0

while True:
    ten = N // 10       # 10의 자리 숫자 구하기 (10으로 나눈 몫)
    one = N % 10        # 1의 자리 숫자 구하기 (10으로 나눈 나머지)
    new_num = ten + one # 10의 자리 숫자와 1의 자리 숫자를 더해 새로운 숫자 생성
    count += 1          # 더하기 사이클은 한 번 완료했기 때문에 +1
    N = int(str(one) + str(new_num % 10))   # 기존의 숫자(one)과 새로 생성된 숫자(new_num)의 1의 자리 숫자를 결합
    if(num == N):       # 처음 입력했던 숫자와 새롭게 결합된 숫자가 같을 경우 while문을 벗어남
        break
print(count)
