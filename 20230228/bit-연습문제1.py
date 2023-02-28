'''
70개 숫자
'''

arr = list(map(int, input()))
N = len(arr)    # 70
num = 0

for i in range(N):
    j = i % 7
    num += arr[i] * (2**(6-j))
    if j == 6:
        print(num, end = ' ')
        num = 0
print()
