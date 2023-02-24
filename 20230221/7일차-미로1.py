def bfs(i, j):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = []
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        ci, cj = queue.pop(0)

        if arr[ci][cj] == 3:    # 도착점(3)에 도착했다면
            return 1  # 도착하면 1

        for d in dir:
            ni, nj = ci + d[0], cj + d[1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[ci][cj] + 1
                queue.append((ni, nj))
    return 0    # 도착하지 못함 0

for _ in range(10):
    N = 16
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    i = j = 1
    print(f'#{tc} {bfs(i, j)}')