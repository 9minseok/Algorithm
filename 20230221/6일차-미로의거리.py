def bfs(i, j):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = []
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        ci, cj = queue.pop(0)

        if arr[ci][cj] == 3:    # 도착점(3)에 도착했다면
            return visited[ci][cj] - 2  # 출발,도착을 제외한 나머지 거리

        for d in dir:
            ni, nj = ci + d[0], cj + d[1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[ci][cj] + 1
                queue.append((ni, nj))
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    si = sj = -1        # 출발점(2) 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                break
        if si != -1:
            break

    print(f'#{tc} {bfs(si, sj)}')