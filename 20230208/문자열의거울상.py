import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    word = input()
    result = ""

    for i in range(len(word)-1, -1, -1):
        if word[i] == 'b':
            result += 'd'
        elif word[i] == 'd':
            result += 'b'
        elif word[i] == 'p':
            result += 'q'
        else :
            result += 'p'

    print(f'#{tc} {result}')