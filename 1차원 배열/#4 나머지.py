num_list = []

for i in range(10):
    num = int(input())
    re = num % 42       # 42로 나눈 나머지
    num_list.append(re) #42로 나눈 나머지를 리스트에 추가

result = set(num_list)  # 중복을 허용하지 않는 set()의 특징을 이용해 중복 제거
print(len(result))      # 중복을 제거한 리스트의 길이(갯수) 출력
