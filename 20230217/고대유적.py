def count(arr):
    maxV = 2
    for li in arr:
        cnt = 0
        for a in li:
            if a == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0
    return maxV

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))

    ans = count(arr)
    ans_t = count(arr_t)

    if ans < ans_t:
        ans = ans_t

    print(f'#{tc} {ans}')