T = int(input())

for tc in range(1, T+1):
    people = list(map(int, input()))
    clap = employ = 0

    for i in range(len(people)):
        if people[i] != 0:

            if clap >= i:
                clap += people[i]
            else:

                employ += i - clap

                clap = i + people[i]

    print(f'#{tc} {employ}')