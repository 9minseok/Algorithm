# 시작 값에서 6의 배수로 증가함

n = int(input())

beehouse = 1
cnt = 1
while n > beehouse :
    beehouse += 6 * cnt
    cnt += 1
print(cnt)