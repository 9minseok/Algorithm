def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):   # 오른쪽으로만 교환이 일어나도록 i부터 k까지
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
N = len(p)
f(0, N)