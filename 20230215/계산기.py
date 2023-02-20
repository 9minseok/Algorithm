'''
2+3*4/5
'''
for tc in range(1,11):
    N = int(input())
    fn = list(input())
    stack = [0] * N
    top = -1
    postfix = ''

    for t in fn:

        if '0' <= t <= '9':     # 피연산자인 경우
            postfix += t
        elif t == '+':               # 연산자인 경우
            if top == -1:     # 스택이 비어있거나 토큰의 우선순위가 높으면
                top += 1    # push
                stack[top] = t
            else:
                while top > -1:         # 스택이 남아있고 토큰의 우선순위가 높을 때 까지
                    top -= 1
                    postfix += stack[top+1]
                top += 1  # push
                stack[top] = t

    while top > -1:
        top -= 1
        postfix += stack[top + 1]

    stack = []
    for i in list(postfix):
        if i.isdigit():  # 숫자
            stack.append(int(i))
        else:  # 연산자
            if len(stack) > 1:  # 연산 가능
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
    result = stack.pop()
    print(f'#{tc}', result)