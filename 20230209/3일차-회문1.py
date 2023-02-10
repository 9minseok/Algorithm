import sys
sys.stdin = open("input.txt", "r")

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(8)]
    ans = []

    for i in range(8): # 가로 서칭
        for j in range(8-N+1):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]: # 뒤집어서 회문인지 확인
                ans.append(arr[i][j:j+N]) # 회문이라면 ans 리스트에 추가


    for i in range(8-N+1): # 세로 서칭
        for j in range(8):
            li = [] # 세로열 문자 넣을 리스트
            for k in range(N):
                li.append(arr[i+k][j])
            if li == li[::-1]:  # 세로줄이 회문이면
                ans.append(''.join(li))

    print(f'#{tc} {len(ans)}')