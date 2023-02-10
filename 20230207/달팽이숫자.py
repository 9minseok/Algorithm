# import sys
# sys.stdin = open("input.txt", "r")

di = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위
dj = [1, 0, -1, 0]
T = int(input())

for tc in range(1, T+1):
    # N * N 빈 배열 생성
    # 다음칸이 없는 경우 방향을 바꿔
    # 숫자가 써져있는 칸을 만나도 방향을 바꿔
    # (k+1) % 4 -> 01230123 반복 (방향)
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dir = 0     # 진행방향
    i = j = 0   # 숫자를 쓸 칸의 인덱스
    for k in range(1, N*N+1):
        arr[i][j] = k
        ni, nj = i+di[dir], j+dj[dir]   # 다음 숫자를 쓸 좌표
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:   # 배열을 벗어나거나 이미 숫자가 있으면
            dir = (dir + 1) % 4     # 방향전환
            i, j = i + di[dir], j + dj[dir]

    print(f'#{tc}')
    for x in arr:
        print(*x)