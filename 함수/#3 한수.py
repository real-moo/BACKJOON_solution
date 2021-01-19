X = int(input())

count = 0

for i in range(1, X + 1): # 1부터 num까지
    if i < 100:           # 1~99까지의 숫자는 모두 한수이다.
        count += 1
    else:
        num = list(map(int, str(i)))  # 100이상의 수를 각 자리수마다 분리한다.
        if num[0] - num[1] == num[1] - num[2]:  # 1,000보다 작은 수이기 때문에 3자리 수
            count += 1
print(count)
