A = int(input())
B = int(input())

print(A*(B%10))         # B의 1의 자리 숫자를 알아내기 위해 10으로 나눠 나머지(5)를 구한 뒤, A와 곱한다.
print(A*((B//10)%10))   # B의 10의 자리 숫자를 알아내기 위해 10으로 나눈 몫(38)에 다시 10으로 나눠 나머지(8)를구한 뒤, A와 곱한다. 
print(A*(B//100))       # B의 100의 자리 숫자를 알아내기 위해 100으로 나눈 몫(3)을 구한 뒤, A와 곱한다.
print(A*B)
