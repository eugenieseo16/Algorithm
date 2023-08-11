import sys


def balancing(sentence):
    stack = []
    for alphabet in sentence:
        if alphabet == "(" or alphabet == "[":
            stack.append(alphabet)
        elif alphabet == ")":
            if len(stack) == 0 or stack.pop() != "(":
                return "no"
        elif alphabet == "]":
            if len(stack) == 0 or stack.pop() != "[":
                return "no"
        elif alphabet == ".":
            if len(stack) == 0:
                return "yes"
            else:
                return "no"


while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    else:
        print(balancing(sentence))
