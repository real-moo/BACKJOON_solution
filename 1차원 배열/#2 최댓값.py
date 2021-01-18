N_list = []
for i in range(9):
    N_list.append(int(input()))

print('{}\n{}'.format(max(N_list), N_list.index(max(N_list))+1))
