# 후위순회
def postorder(i):    # 후위 순회
    global stack
    if tree[i]:
        postorder(left[i])
        postorder(right[i])
        if type(tree[i]) == int:
            stack.append(tree[i])
        else:
            a = stack.pop()
            b = stack.pop()
            if tree[i] == '+':
                stack.append(b+a)
            elif tree[i] == '-':
                stack.append(b-a)
            elif tree[i] == '*':
                stack.append(b*a)
            elif tree[i] == '/':
                stack.append(b/a)
    return

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        info = input().split()
        if len(info) == 4:
            tree[int(info[0])] = info[1]
            left[int(info[0])] = int(info[2])
            right[int(info[0])] = int(info[3])
        else:
            tree[int(info[0])] = int(info[1])

    stack = []
    postorder(1)
    print(f'#{tc} {int(stack[-1])}')