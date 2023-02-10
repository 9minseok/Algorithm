# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     cnts = [0] * 1001
#
#     for _ in range(N):
#         bus_type, S, E = map(int, input().split())
#
#         if bus_type == 1:
#             for i in range(S, E + 1):
#                 cnts[i] += 1
#
#         elif bus_type == 2:
#             if S % 2 == 0:
#                 for i in range(S, E + 1, 2):
#                     cnts[i] += 1
#             else:
#                 for i in range(S, E + 1, 2):
#                     cnts[i] += 1
#
#         elif bus_type == 3:
#             if S % 2 == 0:
#                 for j in range(S, E + 1):
#                     if j % 4 == 0:
#                         cnts[j] += 1
#             else:
#                 for j in range(S, E + 1):
#                     if j % 3 ==0 and j % 10 != 0:
#                         cnts[j] += 1
#
#     maxV = 0
#     for i in range(len(cnts)):
#         if maxV < cnts[i]:
#             maxV = cnts[i]
#     print(cnts)
#     print(f'#{tc} {maxV}')




T = int(input())

for tc in range(1, T+1):
    N = int(input())

    cnts = [0] * 1001

    for _ in range(N):
        bus_type, S, E = map(int, input().split())

        if bus_type == 1:
            for i in range(S, E + 1):
                cnts[i] += 1

        elif bus_type == 2:
            if S % 2 == 0:
                for i in range(S, E + 1):
                    if i == S or i == E:
                        cnts[i] += 1
                    elif i % 2 == 0:
                        cnts[i] += 1
            else:
                for i in range(S, E + 1):
                    if i == S or i == E:
                        cnts[i] += 1
                    elif i % 2 == 1:
                        cnts[i] += 1

        elif bus_type == 3:
            if S % 2 == 0:
                for j in range(S, E + 1):
                    if j == S or j == E:
                        cnts[j] += 1
                    elif j % 4 == 0:
                        cnts[j] += 1
            else:
                for j in range(S, E + 1):
                    if j == S or j == E:
                        cnts[j] += 1
                    elif j % 10 == 0:
                        continue
                    elif j % 3 == 0:
                        cnts[j] += 1

    maxV = 0
    for i in range(len(cnts)):
        if maxV < cnts[i]:
            maxV = cnts[i]

    print(f'#{tc} {maxV}')