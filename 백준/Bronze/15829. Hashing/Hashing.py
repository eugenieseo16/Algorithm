N = int(input())
words = input()
new_words = 0
M = 1234567891
r = 31

for i in range(N):
    new_words += (ord(words[i]) - 96) * (r**i)
print(new_words % M)
