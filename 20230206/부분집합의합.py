import sys
sys.stdin = open("input.txt", "r")

T = int(input())

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T + 1):
    s, k = map(int, (input().split()))
    n = len(arr)
    result = []
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(arr[j])

        if len(temp) == s and sum(temp) == k:
            result += [temp]

    print(f'#{tc} {len(result)}')