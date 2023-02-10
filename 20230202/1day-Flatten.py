T = 10
for tc in range(1, T+1):
    dump_cnt = int(input()) # 상자 이동 가능 횟수
    boxes = list(map(int, input().split())) # 상자들 높이

    for i in range(dump_cnt): # 이동 가능 횟수만큼 반복
        maxV = 1 # 최대값 초기화
        minV = 100 # 최소값 초기화
        maxidx = minidx = 0

        for j in range(100): # 최대값 최소값 , 그 값의 인덱스 구하기
            if maxV < boxes[j]:
                maxV = boxes[j]
                maxidx = j
            if minV > boxes[j]:
                minV = boxes[j]
                minidx = j

        boxes[maxidx] -= 1 # 인덱스로 최대값을 찾아 -1
        boxes[minidx] += 1 # 인덱스로 최소값을 찾아 +1

    # 이동이 끝난 후
    rls_maxV = 1 # 최대값 초기화
    rls_minV = 100 # 최소값 초기화
    for m in range(100): # 최대값 , 최소값 찾기
        if rls_maxV < boxes[m]:
            rls_maxV = boxes[m]
        if rls_minV > boxes[m]:
            rls_minV = boxes[m]

    ans = rls_maxV - rls_minV # 최대 - 최소
    print(f'#{tc} {ans}')