T = int(input())

for i in range(T):
    R, S = input().split()
    Slist = list(map(str, S))
    
    for j in range(len(Slist)):
        result = Slist[j] * int(R)
        print(result, end='')
    print()
