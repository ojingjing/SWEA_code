n = int(input())

for i in range(1,n+1):
    x, y, z = map(int,input().split())
    dif_left = y-x
    dif_right = z-y

    if dif_left == dif_right: print(f'#{i} {0.0}')

    else: print(f'#{i} {abs(dif_left-dif_right)/2}')
