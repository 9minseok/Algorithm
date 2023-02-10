import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    mat = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    for i in range(9):
        sum = 0
        for j in range(9):
            sum += mat[i][j]
        if sum != 45:
            ans = 0
            break

    for j in range(9):
        sum = 0
        for i in range(9):
            sum += mat[i][j]
        if sum != 45:
            ans = 0
            break


    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sum = 0
            for x in range(3):
                for y in range(3):
                    sum += mat[i+x][j+y]
        if sum != 45:
            ans = 0
            break

    print(f'#{tc} {ans}')


