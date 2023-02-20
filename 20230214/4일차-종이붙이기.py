T = int(input())

def paper(N):
    p = [0] * (N+1)
    p[0] = 1
    p[1] = 1
    N = N // 10
    for i in range(2, N+1):
        p[i] = p[i-1] + (2 * p[i-2])

    return p[N]


for tc in range(1, T+1):
    ans = paper(int(input()))
    print(f'#{tc} {ans}')



# 10 20 30 40 50 60 70 80 90 100
# 1  3  5  11 21 43 85

