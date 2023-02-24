cost = [((k * k) + (k - 1) * (k - 1)) for k in range(40)]

def solve_idea():
    mx = 0
    home = []
    for si in range(N):
        for sj in range(N):  # [1] 집의 모든 위치를 저장
            if arr[si][sj] == 1:
                home.append((si, sj))
    # print(home)
    # [2] 각 기준위치에서 거리별 집의 개수 누적하기
    for si in range(N):
        for sj in range(N):  #
            dist = [0] * 40
            # 거리별 집위치를 누적
            for ti, tj in home:
                t = abs(si - ti) + abs(sj - tj) + 1
                dist[t] += 1

            for k in range(1, 40):
                dist[k] += dist[k - 1]
                if cost[k] <= dist[k] * M:
                    mx = max(mx, dist[k])
    return mx


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # M: 비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve_idea()
    print(f'#{test_case} {ans}')
