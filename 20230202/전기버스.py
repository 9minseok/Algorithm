T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int,input().split())
    charge_num = list(map(int, input().split()))
    charge_cnt = cur = 0

    while cur + K < N: # 종점까지 도달할때까지
        for move in range(K, 0, -1): # K 내에서 역순으로 이동
            if (cur + move) in charge_num: # 현재위치 + 이동 = 충전소가 있다면
                cur += move # 현재위치를 이동한 만큼 변경
                # print(cur)
                charge_cnt += 1 # 충전횟수 + 1
                break # for문을 종료함

        # for-else : for문이 break등 중간에 빠져나오지 않았다면 else문을 실행
        else: # 이동 범위내에 충전기가 없다면 -> break문으로 빠져나오지 않았다면
            charge_cnt = 0 # 충전횟수는 0
            break

    # 결과 출력
    print(f'#{tc} {charge_cnt}')