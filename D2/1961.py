t= int(input())

for q in range(t):
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]

    a,b,c=[],[],[]

    for i in range(n):
        value_a = ''
        value_b = ''
        value_c = ''
        for j in range(n-1,-1,-1):        
            value_a+=str(board[j][i])
            value_b+=str(board[n-i-1][j])
            value_c+=str(board[n-j-1][n-i-1])
        a.append(value_a)
        b.append(value_b)
        c.append(value_c)
        
    print(f'#{q+1}')
    for i in range(n):  
        print(f'{a[i]} {b[i]} {c[i]}')