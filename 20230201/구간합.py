T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    maxV = 0
    minV = 1000000

    for i in range(N-M+1):
        s = 0               # i에서 시작하는 구간합
        for j in range(i, i+M):
            s += arr[j]

        if maxV < s:
            maxV = s
        if minV > s:
            minV = s

    print(f'#{tc} {maxV-minV}')
