import sys
sys.stdin = open("input.txt", "r")

def binary_search(page):
    left = 1
    right = P
    ans = 0
    while left <= right:
        mid = int((left + right) / 2)
        if mid == page:
            ans += 1
            break
        elif mid > page:
            right = mid
            ans += 1
        else:
            left = mid
            ans += 1
    return ans

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    A_ans = binary_search(A)
    B_ans = binary_search(B)
    ans = 0
    if A_ans > B_ans:
        ans = 'B'
    elif A_ans < B_ans:
        ans = 'A'
    else:
        ans = 0

    print(f'#{tc} {ans}')