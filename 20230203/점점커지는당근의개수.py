# 연속으로 커지는 수 찾기 (최대)
# 5 <= N <= 1000, 1 <= C <= 10

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = max_cnt = 0

    for i in range(N-1):
        if C[i] + 1 == C[i+1]:
            cnt += 1
        else:
            cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt+1}')
