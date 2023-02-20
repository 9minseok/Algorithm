T = int(input())

for tc in range(1, T+1):
    stack = []
    s = input()

    for i in s:
        if not stack:           # 스택이 비어있으면
            stack.append(i)     # 원소를 추가
        elif stack[-1] == i:    # 넣을 원소가 마지막 값과 같다면
            stack.pop()         # 마지막 원소 빼냄
        else:                   # 아니라면
            stack.append(i)     # 그냥 추가

    print(f'#{tc} {len(stack)}')