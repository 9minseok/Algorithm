# 숫자 N은
# N = 2^a X 3^b X 5^c X 7^d X 11^e 로 정의된다
# a, b, c, d, e 를 출력하라
# 제약사항 : N은 2이상 10,000,000 이하

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    divs = [2, 3, 5, 7, 11] # 나눌 수를 리스트에 저장
    cnts = [0] * len(divs) # 나눈 횟수를 카운트할 리스트 생성

    for i in range(0, len(divs)):
        while N % divs[i] == 0: # 나누어 떨어진다면
            cnts[i] += 1 # 횟수를 카운트하고
            N = N // divs[i] # N을 나눈 수로 나누기

    print(f'#{tc}', *cnts)

