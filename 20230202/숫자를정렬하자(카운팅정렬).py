T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    counts = [0] * (max(arr)+1)
    arr_sort = [0] * N

    for i in range(0, len(arr)):
        counts[arr[i]] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in range(len(arr_sort)-1, -1, -1):
        counts[arr[i]] -= 1
        arr_sort[counts[arr[i]]] = arr[i]

    print(f'#{tc}', *arr_sort)

