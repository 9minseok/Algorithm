T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # arr 네방향 0으로 패딩해서 둘러쌈
    arr = [[0] * (N + 2) for _ in range(N + 2)]
    # [1] 초기 돌 위치 놓기
    m = N // 2
    arr[m][m] = arr[m + 1][m + 1] = 2
    arr[m + 1][m] = arr[m][m + 1] = 1

    # [2] 흑돌 백돌 입력 받아서 처리
    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        # 8방향 처리
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            # 해당 방향으로 뻗어나가면서 처리
            tlst = []
            for mul in range(1, N):
                ni, nj = si + di * mul, sj + dj * mul
                if arr[ni][nj] == 0:  # 빈칸 범위밖..
                    break
                elif arr[ni][nj] != d:  # 다른돌인 경우 뒤집기 후보에 추가
                    tlst.append((ni, nj))
                else:  # 같은돌=>후보들을 뒤집고, 종료
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = d
                    break

    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{test_case} {bcnt} {wcnt}')


############################################################################################

didj = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
op = [0, 2, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    brd = [[0] * (N + 2) for _ in range(N + 2)]
    stone = [list(map(int, input().split())) for _ in range(M)]
    B, W = 1, 2

    brd[N // 2][N // 2] = W
    brd[N // 2][N // 2 + 1] = B
    brd[N // 2 + 1][N // 2] = B
    brd[N // 2 + 1][N // 2 + 1] = W

    for j, i, bw in stone:
        brd[i][j] = bw
        for di, dj in didj:
            flip = []
            ni, nj = i + di, j + dj
            while brd[ni][nj] == op[bw]:
                flip.append((ni, nj))
                ni += di
                nj += dj
            if brd[ni][nj] == bw:  # 같은 색을 만나면 모두 뒤집기
                for ni, nj in flip:
                    brd[ni][nj] = bw
    cnt = [0] * 3
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cnt[brd[i][j]] += 1

    print(f'#{tc} {cnt[B]} {cnt[W]}')
