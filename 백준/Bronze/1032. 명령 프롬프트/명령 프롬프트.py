
N = int(input())
words = []
for _ in range(N):
    words.append(list(input()))
word = words[0]
num = len(word)

for j in range(num):
    for i in range(1, N):
        if word[j] != words[i][j]:
            word[j] = "?"
            break


print("".join(word))
