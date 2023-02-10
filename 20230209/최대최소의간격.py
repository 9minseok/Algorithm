import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = 1
    minV = 10
    max_idx = 0
    min_idx = 0

    for i in range(N):
        if maxV <= arr[i]:
            maxV = arr[i]
            max_idx = i + 1

        if minV > arr[i]:
            minV = arr[i]
            min_idx = i + 1

    print(f'#{tc} {abs(max_idx-min_idx)}')