# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     li = list(map(int, input().split()))[::-1]
#
#     ans = mx = 0
#     for value in li:
#         if mx > value:
#             ans += mx - value
#         else:
#             mx = value
#
#     print(f'#{tc} {ans}')
####################################################
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     maxV = arr[-1] # 마지막값을 최대값으로 저장
#     rlt = 0
#     for i in range(N - 2, -1, -1):
#         if arr[i] > maxV:
#             maxV = arr[i]
#         rlt += maxV - arr[i]
#
#     print(f'#{tc}', rlt)

######################################################
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[-1] # 마지막값을 최대값으로 저장
    rlt = 0
    for i in range(N - 2, -1, -1):
        if arr[i] < maxV:
            rlt += maxV - arr[i]
        maxV = max(maxV, arr[i])
    print(f'#{tc}', rlt)