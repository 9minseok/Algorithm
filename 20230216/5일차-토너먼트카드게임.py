def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i == j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

def win(l, r):
    global cards
    if cards[l] == cards[r]:
        return l
    elif cards[l] == 1:
        if cards[r] == 2:
            return r
        elif cards[r] == 3:
            return l
    elif cards[l] == 2:
        if cards[r] == 1:
            return l
        elif cards[r] == 3:
            return r
    elif cards[l] == 3:
        if cards[r] == 1:
            return r
        elif cards[r] == 2:
            return l

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    winner = f(0, N-1) + 1
    print(f'#{tc} {winner}')
