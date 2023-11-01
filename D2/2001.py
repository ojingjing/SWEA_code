n,m = map(int, input().split())

land = [list(map(int,input().split())) for _ in range(n)]

for i in range(m-1,n):
    for j in range(m-1,n):
        for x in range(j,j-m-1,-1):
            for y in range(x,x-m-1,-1):
                print(land[x][y])