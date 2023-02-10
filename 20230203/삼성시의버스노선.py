# 1에서 5000번까지 번호
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선

# 1. cnts[] 빈도수를 표현 -> 5001개
# Start, End (1,3) (2,5)

# 2. 지정된 정류장 버스 개수
# alst = [], p 입력
# alst.append(cnts[p])

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # N번 반복하면서 노선입력, 빈도수 표시
    cnts = [0] * 5001

    for _ in range(N):
        S, E = map(int, input().split())

        for i in range(S, E+1):
            cnts[i] += 1

    P = int(input())
    alst = []
    for _ in range(P):
        p = int(input())
        alst.append(cnts[p])

    print(f'#{tc}', *alst)