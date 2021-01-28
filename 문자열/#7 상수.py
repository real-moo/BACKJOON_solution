A, B = input().split()
# 입력받은 숫자를 역순으로
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)
