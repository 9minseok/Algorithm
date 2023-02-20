def f(i, k):
    if i == k:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)

A = [i for i in range(1000)]
B = [0] * 1000
f(0 ,1000) # 재귀호출의 최대 깊이를 넘어섬


