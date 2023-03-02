for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    k = cnt = 0
    while k < M:
        k += 1
        for i in range(N):
            for j in range(N):
                if M % k == 0:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    else:
                        arr[i][j] = 0

                elif (i + j + 2) % k == 0:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    else:
                        arr[i][j] = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
    print(f'#{tc} {cnt}')