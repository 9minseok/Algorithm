T = int(input())
for t in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    minV = 200
    ans = 0

    for i in range(len(C)):
        diff = abs(sum(C[:i]) - sum(C[i:]))
        if diff < minV:
            minV = diff
            ans = i

    print(f'#{t + 1} {ans} {minV}')