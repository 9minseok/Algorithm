T = int(input())
for tc in range(1, T + 1):
    li = input().split()
    stack = []

    for i in li:
        if i == '.':  # 종료
            if len(stack) > 1:  # 종료인데 stack에 2개 이상 있다면 error
                result = 'error'
            else:
                result = stack.pop()
            break
        elif i.isdigit():  # 숫자
            stack.append(int(i))
        else:  # 연산자
            if len(stack) > 1:  # 연산 가능
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(int(a / b))
            else:  # 연산 불가능
                result = 'error'
                break

    print(f'#{tc}', result)