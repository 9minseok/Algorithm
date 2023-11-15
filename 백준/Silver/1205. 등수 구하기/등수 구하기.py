# N, 태수의 새로운 점수, P
# 0 <= N <= P
# 10 <= P <= 50
N, score, p = map(int, input().split())


if N == 0:
    print(1)
else:
    rank = list(map(int, input().split()))

    if N == p and rank[-1] >= score:
        print(-1)
    else:
        res = N+1
        for i in range(N):
            if rank[i] <= score:
                res = i + 1
                break
        print(res)
        
