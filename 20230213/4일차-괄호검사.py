T = int(input())

for tc in range(1,T+1):
    stack = []
    s = input()
    ans = 1

    for i in s:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}' or i == ')':
            if stack and i == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and i == ')' and stack[-1] == '(':
                stack.pop()
            else:
                ans = 0
                break

    if stack:
        ans = 0

    print(f'#{tc} {ans}')