T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Ci = list(map(int, input().split()))
    # Ci.sort()
    ans = 0
    m = int(N/2)
    cnt = [0] * 31

    for i in Ci:
        cnt[i] += 1
    # print(cnt)

    if len(set(Ci)) > 2:
        for j in range(len(cnt)):
            if cnt[j] > m:
                ans = -1
                break
            else:
                pass
    else:
        ans = -1
    print(f'#{tc} {ans}')