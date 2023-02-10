T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    counts = [0] * 10 # 카운트배열 생성

    for i in range(0, len(arr)):
        counts[arr[i]] += 1 # 카운트배열에 카드 개수 세기
    maxV = 0
    for i in range(len(counts)):
        if counts[i] > maxV:
            maxV = counts[i]
    for i in range(len(counts)-1, -1, -1):
        if counts[i] == maxV: # 범위를 뒤에서부터 탐색, 카드 수가 같으면 가장 큰 수를 내야하기 때문
            print(f'#{tc} {i} {maxV}')
            break