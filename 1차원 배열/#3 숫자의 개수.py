mul = 1
for i in range(3):
    num = int(input())
    mul *= num

for j in range(10):	# 0~9까지
    result = str(mul).count(str(j))
    print(result)
