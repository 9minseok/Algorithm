N, M = map(int, input().split())


def solve(cnt, s):
    if cnt == M:  # M개를 골랐으면 종료
        print(" ".join(s))
        return

    for num in [str(i) for i in range(1, N + 1)]:
        if num not in s:  # 이미 고르지 않은 숫자를 고르게 함
            solve(cnt + 1, s + [num])


solve(0, [])