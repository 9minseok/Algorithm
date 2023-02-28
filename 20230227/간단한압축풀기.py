T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = [list(input().split()) for _ in range(N)]
    stack = []
    for i in li:
        for j in range(int(i[1])):
            stack.append(i[0])

    print(f'#{tc}')
    while stack:
        for i in range(10):
            if stack:
                s = stack.pop(0)
                print(s, end='')
            else:
                break
        print()

