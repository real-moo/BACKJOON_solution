S = str(input())

for i in range(97, 123):    # 알파벳 소문자의 아스키 코드값의 범위 : 97 ~ 122
    print(S.find(chr(i)), end=' ')
