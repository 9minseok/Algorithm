T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()

    ans = "Possible"

    for i in range(N):
        bread = (people[i] // M) * K - (i + 1)
        if bread < 0:
            ans = "Impossible"
            break

    print(f'#{tc} {ans}')