#import sys
#sys.stdin = open('input.txt')

N = int(input())

def pre_order(tree, start):
    pre_nodes = start
    if tree[ord(start)-65][0] != '.':
        pre_nodes += pre_order(tree, tree[ord(start)-65][0])
    if tree[ord(start)-65][1] != '.':
        pre_nodes += pre_order(tree, tree[ord(start)-65][1])
    return pre_nodes

def in_order(tree, start):
    in_nodes = ''
    if tree[ord(start)-65][0] != '.':
        in_nodes += in_order(tree, tree[ord(start)-65][0])
    in_nodes += start
    if tree[ord(start)-65][1] != '.':
        in_nodes += in_order(tree, tree[ord(start)-65][1])
    return in_nodes

def post_order(tree, start):
    post_nodes = ''
    if tree[ord(start)-65][0] != '.':
        post_nodes += post_order(tree, tree[ord(start)-65][0])
    if tree[ord(start)-65][1] != '.':
        post_nodes += post_order(tree, tree[ord(start)-65][1])
    post_nodes += start
    return post_nodes

tree = list([0,0] for _ in range(N))
for i in range(N):
    root, left, right = input().split()
    tree[ord(root)-65][0] = left
    tree[ord(root)-65][1] = right

pre_nodes = pre_order(tree, 'A')
in_nodes = in_order(tree, 'A')
post_nodes = post_order(tree, 'A')

print(pre_nodes)
print(in_nodes)
print(post_nodes)
