s = list(input().upper())   # 입력 받은 문자를 모두 대문자로 변환
s_list = []

for i in range(65, 91):     # A(65) ~ Z(90)
    s_list.append(s.count(chr(i)))  # 입력한 알파벳의 갯수를 셈

if s_list.count(max(s_list)) >= 2:
    print('?')
else:
    print(chr(s_list.index(max(s_list))+65))
