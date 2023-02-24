def enq(n):
    global last
    last += 1           # 완전이진트리에 마지막 정점을 추가
    heap[last] = n      # 마지막 정점에 저장

    # 부모가 있고, 부모 > 자식 조건 검사를 위해
    c = last
    p = c//2

    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p           # 옮긴 자리에서 부모와 비교하기 위해
        p = c // 2
    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = ans = 0

    for i in li:
        enq(i)

    while last > 1:        # 루트 노드로 갈때까지
        last = last // 2   # 리프노드의 조상으로 올라가
        ans += heap[last]  # 하나씩 더해라

    print(f'#{tc} {ans}')