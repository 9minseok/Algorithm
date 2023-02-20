dir = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

t = int(input())
for tc in range(1, t + 1):
    col, row = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(col)]
    ans = 0

    for y in range(col):
        for x in range(row):
            cnt = 0

            for d in dir:   # 좌표를 기준으로 주변 8방향으로 탐색
                nx, ny = x + d[0], y + d[1]

                # 이동한 좌표가 범위내에 있고, 기준값보다 작다면
                if 0 <= nx < row and 0 <= ny < col and arr[y][x] > arr[ny][nx]:
                    cnt += 1
                if cnt == 4:
                    ans += 1
                    break

    print(f"#{tc} {ans}")