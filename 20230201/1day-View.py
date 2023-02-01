# 조망권 양쪽 2칸 확보
# 가로 길이 항상 1000 이하
# 맨 왼쪽, 오른쪽 두 칸에는 건물 X
# 빌딩 최대 높이 255
T = 10

for tc in range(1, T+1):
    N = int(input()) # 건물의 개수
    arr = list(map(int, input().split())) # 건물의 높이
    ans = 0 # 조망권 확보 건물 개수

    for i in range(2, N-2): # 양쪽 비어있는 두자리 제외
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            # i 건물 기준 왼쪽, 오른쪽 2개 건물 높이와 비교 후 높다면 TRUE

            max_arr = arr[i-2] # 가장 높은 건물 초기화

            for j in range(-2, 3): # 왼쪽 2개, 오른쪽 2개 순회
                if j == 0: # 자기자신 제외 -> 가장 높기 때문
                    continue
                if arr[i - j] > max_arr: # 초기값보다 크다면
                    max_arr = arr[i - j] # 가장 높은 건물을 변경

            ans += arr[i] - max_arr # 건물[i] - (주변 건물 중 가장 큰 건물)

    print(f'#{tc} {ans}')

