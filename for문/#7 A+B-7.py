T = int(input())

for i in range(1, T+1):
    num1, num2 = map(int, input().split())
    print('Case #%d: %d'%(i, num1+num2))
