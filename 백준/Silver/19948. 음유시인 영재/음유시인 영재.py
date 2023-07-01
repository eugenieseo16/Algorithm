

checking_word = input()
poem = checking_word.split()
space = int(input())
possible = list(map(int, input().split()))

title = ''
for word in poem:
    title += word[0].upper()

answer = 0
space_count = len(poem) - 1
if space_count > space:
    answer = -1

num_checking_word = len(checking_word)
if answer != -1:
    for num in range(num_checking_word):
        if checking_word[num] != ' ':
            if num == 0 or checking_word[num-1] != checking_word[num]:
                if possible[(ord(checking_word[num].upper())-65)] <= 0 :
                    answer = -1
                    break
                else:
                    possible[(ord(checking_word[num].upper())-65)] -= 1

num_title_word = len(title)
if answer != -1:
    for n in range(num_title_word):
        if n == 0 or title[n-1] != title[n]:
            if possible[(ord(title[n])-65)] <= 0 :
                answer = -1
                break
            else:
                possible[(ord(title[n])-65)] -= 1

if answer != -1:
    answer = title
print(answer)
