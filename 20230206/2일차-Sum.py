import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):

    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum3 = sum4 = 0
    totalsum = []
    for i in range(100):
        sum1 = sum2 = 0
        for j in range(100):
            sum1 += arr[i][j]
            sum2 += arr[j][i]
        totalsum.append(sum1)
        totalsum.append(sum2)

    for i in range(100):
        sum3 += arr[i][i]
    totalsum.append(sum3)

    for i in range(100):
        sum4 += arr[i][99 - i]
    totalsum.append(sum4)

    ans = max(totalsum)

    print("#{} {}".format(T, ans))
