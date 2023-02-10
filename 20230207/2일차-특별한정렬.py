import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N - 1):  # 작업 구간의 시작인덱스
        Idx = i  # 초기화
        if i % 2 == 0:
            for j in range(i + 1, N):
                if arr[Idx] < arr[j]:
                    Idx = j
            arr[Idx], arr[i] = arr[i], arr[Idx]
        else:
            for j in range(i + 1, N):
                if arr[Idx] > arr[j]:
                    Idx = j
            arr[Idx], arr[i] = arr[i], arr[Idx]

    print(f'#{tc}',*arr[:10])