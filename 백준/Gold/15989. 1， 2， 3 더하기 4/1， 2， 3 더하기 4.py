# 1, 2, 3 더하기 4

# 1의 합으로 정수 n을 나타내는 방법은 1가지
dp = [1] * 10001

# 1, 2의 합으로 정수 n을 나타내는 방법은 (n-2)를 1의 합만으로 나타낸 방법 + 2를 더해줌
# 1, 2, 3의 합으로 정수 n을 나타내는 방법은 (n-3)을 1, 2의 합으로 나타낸 방법 + 3

for i in range(2, 10001):
    dp[i] += dp[i -2]

for i in range(3, 10001):
    dp[i] += dp[i -3]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])