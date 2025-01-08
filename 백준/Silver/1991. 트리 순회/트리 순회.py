n = int(input())

tree = {}

for _ in range(n):
    node, left, right = map(str, input().split())
    tree[node] = [left, right]

def preorder(x):
    if x != '.':
        print(x, end='')
        preorder(tree[x][0])
        preorder(tree[x][1])

def inorder(x):
    if x != '.':
        inorder(tree[x][0])
        print(x, end='')
        inorder(tree[x][1])

def postorder(x):
    if x != '.':
        postorder(tree[x][0])
        postorder(tree[x][1])
        print(x, end='')


preorder('A')
print('')
inorder('A')
print('')
postorder('A')