def inorder(n):  # 중위순회
    if n <= N:
        inorder(n*2)
        print(tree[n], end='')
        inorder(n*2+1)

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):
        li = list(input().split())
        tree[i+1] = li[1]   # 순서대로 문자열을 추가

    print(f'#{tc}', end=' ')
    inorder(1)
    print()