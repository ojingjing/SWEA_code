t = int(input())

for j in range(t):
    n = int(input())
    dd = []
    for i in range(1, int(n**(0.5)+1)):
        if n % i == 0:
            dd.append(i)
            if i != n // i:
                dd.append(n // i)
    dd.sort()

    value = 0
    if len(dd) == 2:
        print(f'#{j + 1} {(dd[0] - 1) + (dd[1] - 1)}')
    elif len(dd) % 2 == 0:
        value = len(dd) // 2
        print(f'#{j + 1} {(dd[value - 1] - 1) + (dd[value] - 1)}')

    else:
        value = len(dd) // 2
        print(f'#{j + 1} {(dd[value] - 1) + (dd[value] - 1)}')


