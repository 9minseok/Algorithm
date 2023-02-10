import sys
sys.stdin = open("input.txt", "r")

T = 10

for _ in range(1, T+1):
    tc = int(input())
    arr = [input() for _ in range(100)]
    ans = []
    for N in range(1,101):
        for i in range(100): # 가로 서칭
            for j in range(100-N+1):
                if arr[i][j:j+N] == arr[i][j:j+N][::-1]: # 뒤집어서 회문인지 확인
                    ans.append(len(arr[i][j:j+N])) # 회문이라면 ans 리스트에 추가


        for i in range(100-N+1): # 세로 서칭
            for j in range(100):
                li = [] # 세로열 문자 넣을 리스트
                for k in range(N):
                    li.append(arr[i+k][j])
                if li == li[::-1]:  # 세로줄이 회문이면
                    ans.append(len(''.join(li)))

    print(f'#{tc} {max(ans)}')