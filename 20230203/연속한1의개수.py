# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값 출력
# 1 <= T <= 10, 10 <= N <= 1000
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    ans = cnt = 0

    for i in range(N):
        if arr[i] == 0:
            cnt = 0
        else:
            cnt += 1
            if ans < cnt: # 최대값 갱신
                ans = cnt

    print(f'#{tc}', ans)
