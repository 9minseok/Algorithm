def arr_min_sum(i, total_sum):
    global minS

    if i == N:  # 행 다 돌았으면
        if total_sum < minS:
            minS = total_sum
            return

    if total_sum > minS:
        return

    for j in range(N):
        if j not in visited:
            visited.append(j)
            arr_min_sum(i+1, total_sum+mat[i][j])
            visited.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    minS = 27

    visited = [] # 열 방문
    arr_min_sum(0, 0)

    print(f'#{tc} {minS}')