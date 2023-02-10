import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # tc

for tc in range(1, T + 1):
    N = int(input())  # N*N의 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * (N + 1)
    findmax = [0] * (N + 1)

    for i in range(N):
        cnt[sum(arr[i])] += 1

    for i in range(1, N):
        findmax[i] = cnt[i] * i

    maxV = 0
    for i in range(N):
        if findmax[i] > maxV:
            maxV = findmax[i]

    print(f'#{tc} {maxV}')