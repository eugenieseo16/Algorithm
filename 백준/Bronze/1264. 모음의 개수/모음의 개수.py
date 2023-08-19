import sys
def counting(words):
    count = 0
    for word in words:
        if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
            count += 1
    print(count)


while True:
    words = input()
    if words == "#":
        break
    else:
        words = words.lower()
        counting(words)
