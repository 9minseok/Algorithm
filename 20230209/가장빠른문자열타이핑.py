# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    len_A = len(A)
    len_B = len(B)
    cur = ans = 0                        # 커서와 누르는 횟수

    while cur < len_A:                   # 전체 문자열을 다 탐색할 동안 반복
        if A[cur] == B[0]:               # 현재 위치와 패턴의 첫 문자가 같다면
            if A[cur:cur+len_B] == B:    # 패턴 길이만큼 전체 문자열에서도 탐색
                ans += 1                 # 누른 횟수 카운트 1
                cur += len_B             # 현재 위치를 패턴 길이만큼 옮김
            else:                        # 같지 않다면
                ans += 1                 # 누른 횟수 카운트 1
                cur += 1                 # 현재 위치 한칸 뒤로
        else:                            # 현재 위치와 패턴의 첫 문자가 같지 않다면
            ans += 1                     # 누른 횟수 카운트 1
            cur += 1                     # 현재 위치 한칸 뒤로

    print(f'#{tc} {ans}')