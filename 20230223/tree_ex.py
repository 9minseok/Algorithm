'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(i):    # 전위 순회
    if i:
        print(i, end=' ')
        preorder(left[i])
        preorder(right[i])
    return

def inorder(i):     # 중위 순회
    if i:
        inorder(left[i])
        print(i, end=' ')
        inorder(right[i])
    return

def postorder(i):    # 후위 순회
    if i:
        postorder(left[i])
        postorder(right[i])
        print(i, end=' ')
    return

V = int(input())
arr = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)
right = [0] * (V+1)
# child = [[] for _ in range(V+1)]

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    # child[p].append(c)

root = 1
while par[root] != 0:
    root += 1
print(root)
preorder(root)