T = int(input())

for tc in range(1, T + 1):

    n = int(input())

    for x in range(1, (10 ** 6) + 1):
        if x ** 3 == n:
            print(f'#{tc} {x}')
            break
    else:
        print(f'#{tc} -1')