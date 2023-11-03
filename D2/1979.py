t =int(input())

for t in range(t):
    n,m= map(int,input().split())
    test = [list(map(int,input().split())) for _ in range(n)]
    count =0 
    for i in range(n):
        x,y =0,0
        for j in range(n):
            if test[i][j] ==1 :
                x +=1
            if test[i][j] ==0 or j ==n-1:
                if x == m :
                    count +=1
                x = 0
            
            if test[j][i] ==1:
                y +=1
            if test[j][i] ==0 or j ==n-1:
                if y == m :
                    count +=1
                y = 0
        
    print(f'#{t+1} {count}')
