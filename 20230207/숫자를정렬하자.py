import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N - 1):  # 작업 구간의 시작인덱스
        minIdx = i  # 맨 앞이 최소라 가정
        for j in range(i + 1, N):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[minIdx], arr[i] = arr[i], arr[minIdx]

    print(f'#{tc}',*arr)