T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    dir = [(0,1), (1,0), (1,-1), (1,1)]
    cnt = 0
    ans = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1

                for d in dir:
                    cnt = 1
                    ni = i + d[0]
                    nj = j + d[1]

                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += d[0]
                        nj += d[1]

                    if cnt == 5:
                        ans = 'YES'

    print(f'#{tc} {ans}')