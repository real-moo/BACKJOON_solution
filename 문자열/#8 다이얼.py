s = list(map(str, input()))     # 받은 문자열을 한 문자씩 리스트에 저장
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for i in s:
    for j in dial:
        if i in j:
            result += dial.index(j)+3

print(result)
