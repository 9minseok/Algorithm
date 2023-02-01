T = int(input())

for tc in range(1, T + 1):
    mat = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(mat):
        cnt = 0

        for j in range(i + 1, mat):

            if arr[i] > arr[j]:
                cnt += 1
        if cnt > ans:
            ans = cnt

    print(f'#{tc} {ans}')
