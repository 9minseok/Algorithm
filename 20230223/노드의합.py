T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for i in range(M):
        node, num = map(int, input().split())
        tree[node] = num

    if N % 2 == 0:      # 노드의 개수가 짝수라면
        tree.append(0)  # 0을 추가

    for i in range((N//2)*2, 1, -2):
        tree[i//2] = tree[i] + tree[i+1]

    print(f'#{tc} {tree[L]}')