H, M = map(int, input().split())

if 23 < H:
    print("23이하의 숫자를 입력해주세요.")
elif 59 < M:
    print("59이하의 숫자를 입력해주세요.")
else:
    M -= 45
    if M < 0:
        H -= 1
        if H < 0:
            H += 24
        M += 60
        print(H, M)
