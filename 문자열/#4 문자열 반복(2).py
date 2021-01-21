T = int(input())  # 테스트 케이스

for i in range(T):
    R, S = input().split()
    Slist = str(S)
    
    for j in range(len(Slist)):
        result = Slist[j] * int(R)
        print(result, end='')
    print()
