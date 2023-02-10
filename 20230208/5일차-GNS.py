import sys
sys.stdin = open("input.txt", "r")

num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())

for tc in range(1, T+1):
    N, length = input().split()
    length = int(length)
    arr = list(map(str, input().split()))
    ans = []

    for i in range(10):  # num 리스트 반복
        for j in arr: # 테스트 케이스 수만큼 반복
            if num[i] == j:
                ans.append(j)

    print(f'#{tc}',*ans)
