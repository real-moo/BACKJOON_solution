def d(n):
    return n + sum(list(map(int, str(n))))

a = [0]*10001

for i in range(1, 10001):
    a[i] = d(i)
   
for i in range(1, 10001):
    if i not in a:
        print(i)
