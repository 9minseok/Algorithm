T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    Q_list = [list(map(int, input().split())) for _ in range(Q)]
    li = [0] * N
    for i in range(1, Q+1):
        for j in range(Q_list[i-1][0]-1, Q_list[i-1][1]):
            li[j] = i

    print(f'#{tc}', *li)