s = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in croatia:
    count += s.count(i) # 크로아티아 알파벳의 개수를 셈

print(len(s)-count)     # 문자열 s의 전체 길이에서 크로아티아 알파뱃의 개수를 뺌
