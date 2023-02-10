# import sys
# sys.stdin = open("input.txt", "r")
#
# di = [-1, 0, 0] # 위, 오른쪽, 왼쪽
# dj = [0, 1, -1]
#
# for _ in range(10):
#     tc = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     i = j = 0
#     for i in range(100):
#         if arr[i][0] == 1:
#             dir = 1
#     dir = 0
#
#     print(arr)
    #print(f'#{tc} {ans}')
import sys

sys.stdin = open("input.txt")


dr = [-1, 0, 0] # 위 0, 오른쪽 1, 왼쪽 2
dc = [0, 1, -1]

T = 10
for _ in range(10):
    tc = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2: # 도착위치(2) 찾기
            ans = i

    dir = 0  # 방향 위로
    row_idx = 99
    while True:
        if row_idx == 0: # 행이 0이 되면 break
            break

        if arr[row_idx][ans - 1]:  # 왼쪽 길이 있을 경우
            dir = 2 # 방향전환
            while True:
                row_idx += dr[dir]
                ans += dc[dir]
                if arr[row_idx][ans-1] == 0:  # 0을 만날때까지 이동
                    break

        elif arr[row_idx][ans + 1]: # 오른쪽 길이 있을 경우
            dir = 1 # 방향전환
            while True:
                row_idx += dr[dir]
                ans += dc[dir]
                if arr[row_idx][ans+1] == 0:  # 0을 만날때 까지 이동
                    break

        dir = 0  # 위로 올라가기
        row_idx += dr[dir]
        ans += dc[dir]

    print(f'#{tc} {ans-1}')