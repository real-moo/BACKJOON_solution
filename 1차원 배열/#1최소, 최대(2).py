N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()       # sort()를 활용하여 오름차순 정렬

print(N_list[0], N_list[N-1])
