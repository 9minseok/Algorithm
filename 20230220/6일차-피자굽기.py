
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))  # 화덕 크기, 피자 개수
    cheese = list(map(int, input().split()))
    pizza = []
    for i in range(M):
        pizza.append([i+1, cheese[i]])  # [피자번호, 치즈양]

    inside_pizza = pizza[:N]        # 화덕크기만큼
    outside_pizza = pizza[N:]       # 남은 피자

    while len(inside_pizza) > 1:    # 하나 남을 때 까지
        check = inside_pizza.pop(0)   # 화덕내부의 맨앞 피자 선택
        check[1] //= 2      # 치즈양 // 2
        if check[1] == 0:   # 치즈양이 0이 됐을 때
            if outside_pizza:   # 화덕외부에 남은 피자가 있다면
                inside_pizza.append(outside_pizza.pop(0))   # 피자 추가
        else:
            inside_pizza.append(check)  # 치즈남아있으면 다시 넣음

    print(f'#{tc} {inside_pizza[0][0]}')