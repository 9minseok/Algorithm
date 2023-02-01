'''
3
5
55 7 78 12 42
6
55 7 100 12 42 1
7
55 7 78 12 42 2 90
가장 큰 값을 출력
#1 78
#2 100
#3 90
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[0]
    for i in range(1, N):
        if maxV < arr[i]:
            maxV = arr[i]
    print(f'#{tc} {maxV}')
