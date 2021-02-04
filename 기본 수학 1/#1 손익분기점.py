A, B, C = map(int, input().split())   # A = 고정비용, B = 가변비용, C = 판매금액

if B >= C:
    print(-1)
else:
    result = A // (C - B)
    print(result+1)
