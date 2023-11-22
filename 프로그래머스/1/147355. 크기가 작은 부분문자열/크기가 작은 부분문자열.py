def solution(t, p):
    answer = 0
    plen = len(p)
    tlen = len(t)
    p = int(p)
    for i in range(0, tlen + 1 - plen):
        if int(t[i : i + plen]) <= p:
            answer += 1
    
    return answer