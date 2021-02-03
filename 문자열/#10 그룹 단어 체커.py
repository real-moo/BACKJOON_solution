num = int(input())
count = 0

for i in range(num):
    word = input()

    for j in range(len(word)):
        if j != len(word) - 1:
            if word[j] == word[j+1]:    # j번째 단어와 j+1번째 단어가 같다면 pass
                pass
            elif word[j] in word[j+1: ]:    # j번째 단어가 j+1번째 단어 이후에 또 나온다면 (연속단어가 아니기 때문에) break
               break
        else:
            count += 1
            
print(count)
