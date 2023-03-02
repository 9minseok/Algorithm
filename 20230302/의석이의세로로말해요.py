# 칠판에 있는 다섯 개의 단어를 세로
# 자리에 글자가 없으면, 읽지 않고 그 다음 글자로

T = int(input())
for tc in range(1, T+1):

    words = [input() for _ in range(5)]

    maxV = 0
    for word in words:
        if len(word) > maxV:
            maxV = len(word)

    ans = ''
    for i in range(maxV):
        for j in range(5):
            if i < len(words[j]):
                ans += words[j][i]

    print(f'#{tc} {ans}')