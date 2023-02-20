for _ in range(10):
    tc = int(input())
    password = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5:   # 5보다 커지면 다시 사이클 순환
            i = 1
        num = password.pop(0) - i   # 첫번째 값 - i 를 num에 저장
        if num <= 0:                # num이 0보다 작다면
            password.append(0)      # 0을 append
            break
        password.append(num)
        i += 1

    print(f'#{tc}',*password)