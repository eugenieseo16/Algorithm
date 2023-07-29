from collections import defaultdict

words = input()
words_list = defaultdict(int)

for word in words:
    words_list[word.upper()] += 1

ans = [k for k, v in words_list.items() if v == max(words_list.values())]
if len(ans) > 1:
    print("?")
else:
    print(ans[0])
