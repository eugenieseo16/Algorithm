words = []
for _ in range(5):
    words.append(list(input()))
ans = ""
max_length = max(len(word) for word in words)
for j in range(max_length):
    for i in range(5):
        if words[i]:
            ans += words[i][0]
            words[i].pop(0)
print(ans)
