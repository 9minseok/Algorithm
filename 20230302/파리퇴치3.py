T = int(input())

type1 = [(-1,0), (1,0), (0,-1), (0,1)]      # + 모양
type2 = [(-1,-1), (-1,1), (1,-1), (1,1)]    # x 모양

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N):
        for j in range(N):
            type1_kill = [arr[i][j]]
            type2_kill = [arr[i][j]]

            for k in range(4):
                for mul in range(1, M):
                    ni = i + mul * type1[k][0]
                    nj = j + mul * type1[k][1]
                    if 0 <= ni < N and 0 <= nj < N:
                        type1_kill.append(arr[ni][nj])
                    nii = i + mul * type2[k][0]
                    njj = j + mul * type2[k][1]
                    if 0 <= nii < N and 0 <= njj < N:
                        type2_kill.append(arr[nii][njj])

            if sum(type1_kill) > maxV:
                maxV = sum(type1_kill)
            elif sum(type2_kill) > maxV:
                maxV = sum(type2_kill)

    print(f'#{tc} {maxV}')