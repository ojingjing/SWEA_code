n = int(input())


for a in range(1,n+1):
    m = int(input())
    print("#"+str(a))
    pascal = [[1 for _ in range(i)] for i in range(1,m+1)]

    for i in range(2,m):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]

    for i in pascal:

        print(*i)