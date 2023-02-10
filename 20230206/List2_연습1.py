def abs(a):
    return a if a>=0 else -a

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [(list(map(int,input().split()))) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ans = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    # print(i, j, ni, nj)
                    ans += abs(arr[i][j] - arr[ni][nj])

    print(f'#{tc} {ans}')
