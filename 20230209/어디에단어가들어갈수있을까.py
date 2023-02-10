import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for i in range(N): # 행부터 탐색
        cnt = 0
        for j in range(N):
            if mat[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0
        if cnt == K:
            total += 1


    for j in range(N): # 열부터 탐색
        cnt = 0
        for i in range(N):
            if mat[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0
        if cnt == K:
            total += 1

    print(f'#{tc} {total}')