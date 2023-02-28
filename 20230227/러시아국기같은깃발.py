T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    side_cnt = middle_cnt = total_cnt = 0

    for i in range(len(arr[0])):    # 맨 윗줄 W
        if arr[0][i] != 'W':
            side_cnt += 1
    for i in range(len(arr[-1])):   # 맨 아랫줄 R
        if arr[-1][i] != 'R':
            side_cnt += 1

    sum_list = []
    NN = len(arr) - 2
    for i in range(NN):
        for j in range(1, NN-i+1):
            for k in range(NN-i-j,-1,-1):
                if i+j+k == NN:
                    middle_cnt = 0
                    for iw in range(i):
                        middle_cnt += len(arr[1+iw]) - arr[1+iw].count('W')
                    for ib in range(j):
                        middle_cnt += len(arr[1+i+ib]) - arr[1+i+ib].count('B')
                    for ir in range(k):
                        middle_cnt += len(arr[1+i+j+ir]) - arr[1+i+j+ir].count('R')
                    sum_list.append(middle_cnt)

    total_cnt = min(sum_list) + side_cnt

    print(f'#{tc} {total_cnt}')