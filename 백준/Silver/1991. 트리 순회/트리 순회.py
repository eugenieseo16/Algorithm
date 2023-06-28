

N = int(input())

def pre_order(tree, start):
    left, right = tree[ord(start) - 65]
    pre_nodes = start
    if left != '.':
        pre_nodes += pre_order(tree, left)
    if right != '.':
        pre_nodes += pre_order(tree, right)
    return pre_nodes

def in_order(tree, start):
    left, right = tree[ord(start) - 65]
    in_nodes = ''
    if left != '.':
        in_nodes += in_order(tree, left)
    in_nodes += start
    if right != '.':
        in_nodes += in_order(tree, right)
    return in_nodes

def post_order(tree, start):
    left, right = tree[ord(start) - 65]
    post_nodes = ''
    if left != '.':
        post_nodes += post_order(tree, left)
    if right != '.':
        post_nodes += post_order(tree, right)
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
