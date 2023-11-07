# 턴 번갈아가면서 1개 또는 3개 가져감
# 마지막 가져간 사람이 승리
# 이기는 사람을 구하라 - 상근(SK)이 먼저 시작, 창영(CY)은 다음

N = int(input()) # 5
 

dp = [0] * (1000 + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 1 
 
for n in range(4, N+1):
    dp[n] = min(dp[n-1], dp[n-3]) + 1
 
if dp[N] % 2 == 1:
    print('SK')
else:
    print('CY')