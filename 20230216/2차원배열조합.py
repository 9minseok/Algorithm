def arr_min_sum(i, total_sum):
    global sum_list
    global cnt

    if i == N:  # 행 다 돌았으면
        cnt += 1
        sum_list.append(total_sum)  # 리스트에 합 추가
        return

    for j in range(N):  # 배열 돌기
        if j not in visited:
            visited.append(j)
            arr_min_sum(i + 1, total_sum + mat[i][j])
            visited.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []   # 원소들의 합을 저장할 리스트
    visited = []  # 열 방문
    cnt = 0
    arr_min_sum(0, 0)
    print(f'#{tc}',min(sum_list))
    print(cnt)