N = int(input())
tree = {}
for _ in range(N):
    mom, left, right = map(str, input().split())
    tree[mom] = [left, right]

def preorder(mom): # 전위 순회
    if mom != '.':
        print(mom, end='')
        preorder(tree[mom][0])
        preorder(tree[mom][1])

def inorder(mom): # 중위 순회
    if mom != '.':
        inorder(tree[mom][0])
        print(mom, end='')
        inorder(tree[mom][1])

def postorder(mom): # 후위순회
    if mom != '.':
        postorder(tree[mom][0])
        postorder(tree[mom][1])
        print(mom, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')