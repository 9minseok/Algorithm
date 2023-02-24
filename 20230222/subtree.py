T = int(input())

def inorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    # print(node)
    inorder(left[node])
    inorder(right[node])

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    left = [0] * (V+1)
    right = [0] * (V+1)
    cnt = 0

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    inorder(N)
    print(f'#{tc} {cnt}')