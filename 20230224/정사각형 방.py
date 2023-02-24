T = int(input())
dir = [(-1,0), (1,0), (0,-1), (0,1)]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0] * ((N**2)+1)

    for i in range(N):
        for j in range(N):
            for d in dir:
                ni, nj = i + d[0], j + d[1]

                if 0<=ni<N and 0<=nj<N and arr[ni][nj]-arr[i][j] == 1:
                    cnt[arr[i][j]] = 1
                    break

    # 연속한 1의 개수 중 가장 긴 경우 찾기, 길이가 같으면 시작 인덱스가 작은 것
    maxIdx = 0
    maxV = 0
    ones = 0
    for i in range(N * N, 0, -1):
        if cnt[i] == 1:
            ones += 1
            if maxV <= ones:
                maxV = ones
                maxIdx = i
        else:
            ones = 0

    print(f'#{tc} {maxIdx} {maxV + 1}')
