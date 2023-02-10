import sys
sys.stdin = open("input.txt", "r")

di = [0, 1, 0, -1]  # 오, 아래, 왼, 위
dj = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    maxV = 0

    for i in range(N):
        for j in range(M):
            total_sum = 0
            for k in range(1, arr[i][j] + 1):
                for l in range(4):
                    ni = i + di[l] * k
                    nj = j + dj[l] * k
                    na = arr[i][j]
                    if 0 <= ni < len(arr) and 0 <= nj < len(arr[0]):
                        total_sum += arr[ni][nj]
                if na + total_sum > maxV:
                    maxV = na + total_sum

    print(f'#{tc} {maxV}')
