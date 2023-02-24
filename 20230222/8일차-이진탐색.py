def binary_tree(n):     # 중위순회
    global cnt

    if n <= N:  # N보다 작을 때만
        binary_tree(n*2)        # left node
        tree[n] = cnt           # 순서대로 대입
        cnt += 1
        binary_tree(n*2 + 1)    # right node

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0 for i in range(N+1)]
    cnt = 1         # 1부터 대입
    binary_tree(1)  # 노드 번호 루트 1

    print(f'#{tc} {tree[1]} {tree[N//2]}')