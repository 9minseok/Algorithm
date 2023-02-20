T = int(input())
for tc in range(1, T + 1):
    stick = input()
    ans = cnt = 0

    for i in range(len(stick)):
        if stick[i] == '(':
            cnt += 1
        else:
            if stick[i - 1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1

    print(f'#{tc} {ans}')