'''
V = 13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

'''
pre(i)
    if i > 0
    print(i)
    pre(c1[i])
    pre(c2[i])
'''

def inorder(idx):
    if idx > N:
        return
    # if left node exists
    if (idx * 2) <= N:
        inorder(idx * 2)
    # append node value to ans
    ans.append(node[idx])
    # if right node exists
    if (idx *2 + 1) <= N:
        inorder(idx * 2 + 1)

for tc in range(10):
    N = int(input())
    node = [0] * (N+1)
    for n in range(N):
        vals = list(input().split())
        node[int(vals[0])] = vals[1]
    ans = []
    inorder(1)
    print("#{} {}".format(tc +1, ''.join(ans)))