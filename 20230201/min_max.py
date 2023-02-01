T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = minV = arr[0]

    for i in range(N):
        if maxV < arr[i]:
            maxV = arr[i]
        if minV > arr[i]:
            minV = arr[i]

    print(f'#{tc} {maxV-minV}')
