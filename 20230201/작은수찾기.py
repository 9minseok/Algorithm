# 가장 작은 수는 몇번째에 있는지
'''
3
5
5 4 3 2 1
5
5 5 5 5 5
5
1 2 3 4 5
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    minV = 10

    for i in range(len(arr)):
        if minV > arr[i]:
            minV = arr[i]

    for i in range(len(arr)):
        if arr[i] == minV:
            cnt += 1
            break
        else:
            cnt += 1

    print(f'#{tc} {cnt}')

