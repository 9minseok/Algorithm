import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    ans = []

    for i in range(N): # 가로 서칭
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]: # 뒤집어서 회문인지 확인
                ans.append(arr[i][j:j+M]) # 회문이라면 ans 리스트에 추가


    for i in range(N-M+1): # 세로 서칭
        for j in range(N):
            li = [] # 세로열 문자 넣을 리스트
            for k in range(M):
                li.append(arr[i+k][j])
            if li == li[::-1]:  # 세로줄이 회문이면
                ans.append(''.join(li))

    print(f'#{tc}',*ans)