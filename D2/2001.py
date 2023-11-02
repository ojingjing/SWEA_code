n,m = map(int, input().split())

land = [list(map(int,input().split())) for _ in range(n)]
result = []
for i in range(m-1,n):
    for j in range(m-1,n):
        result = land[i][j] + land[i-] 