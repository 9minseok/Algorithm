T = int(input())

for tc in range(1, T+1):
    front = -1
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = [0] * (M+1)
    for i in range(M+1):
        front += 1
        queue[i] = arr[front % N]

    print(f'#{tc} {queue[-1]}')