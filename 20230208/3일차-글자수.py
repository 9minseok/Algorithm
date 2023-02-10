import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str_dic = {}
    ans = 0

    for i in str1:
        str_dic[i] = 0

    for j in str2:
        if j in str_dic:
            str_dic[j] += 1

    for k in str_dic:
        ans = max(ans, str_dic[k])

    print(f'#{tc} {ans}')


# T = int(input())
#
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#     str_dic = {}
#
#     for i in str1:
#         str_dic[i] = 0
#
#     for j in str2:
#         if j in str_dic:
#             str_dic[j] += 1
#
#     maxV = max(str_dic)  # ????
#
#     print(f'#{tc} {str_dic[maxV]}')