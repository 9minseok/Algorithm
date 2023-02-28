hex_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100',
           '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001',
           'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

change_code = {'112':'0', '122':'1', '221':'2',
               '114':'3', '231':'4', '132':'5',
               '411':'6', '213':'7', '312':'8',
               '211':'9'}


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    arr = list(set(arr))    # 중복 제거
    # print(arr)
    secret_code = ''
    V_code = []
    ans = 0

    for i in range(len(arr)):   # 16진수 -> 2진수로 변환
        binary = ''
        for c in arr[i]:
            binary += hex_bin[c]
        arr[i] = binary
    # print(arr)

    tmp_code = ''
    for i in range(len(arr)):
        ratio1 = ratio2 = ratio3 = 0

        for j in range(len(arr[i])-1, -1, -1):  # 16진수를 2진수로 바꿨으므로 가로 범위를 새로 지정
            if ratio2 == 0 and ratio3 == 0 and arr[i][j] == '1':
                ratio1 += 1
            elif ratio1 and ratio3 == 0 and arr[i][j] == '0':
                ratio2 += 1
            elif ratio1 and ratio2 and arr[i][j] == '1':
                ratio3 += 1
            elif ratio3 and arr[i][j] == '0':
                minV = min(ratio1, ratio2, ratio3)   # 비율을 계산하기 위해 최소값 계산
                tmp_code += change_code[str(ratio1//minV)+str(ratio2//minV)+str(ratio3//minV)]
                ratio1 = ratio2 = ratio3 = 0
                # print(tmp_code)

                if len(tmp_code) == 8:  # 검증코드 8자리가 다 들어왔다면
                    for n in range(len(tmp_code)-1, -1, -1):    # 뒤에서부터 다시 정렬
                        secret_code += str(tmp_code[n])
                    # print(secret_code)
                    if secret_code not in V_code:   # 암호코드가 이전에 검증한 코드에 없다면
                        tmp = (( int(secret_code[0]) + int(secret_code[2]) + int(secret_code[4]) + int(secret_code[6])) * 3 ) + (int(secret_code[1]) + int(secret_code[3]) + int(secret_code[5]) + int(secret_code[7]))
                        if tmp % 10 == 0:
                            ans += ( int(secret_code[0]) + int(secret_code[1]) + int(secret_code[2]) + int(secret_code[3]) + int(secret_code[4]) + int(secret_code[5]) + int(secret_code[6]) + int(secret_code[7]) )
                        V_code.append(secret_code)
                        # print(tmp)
                    tmp_code = ''
                    secret_code = ''
    print(f'#{tc} {ans}')