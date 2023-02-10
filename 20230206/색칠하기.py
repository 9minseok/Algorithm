import sys
sys.stdin = open("input.txt", "r")

T = int(input())


for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    cnt = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += 1 # 주어진 영역에 1씩 추가

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2: # 주어진 영역이 겹쳤더라면 2가 저장됐으므로
                cnt += 1

    print(f'#{tc} {cnt}')