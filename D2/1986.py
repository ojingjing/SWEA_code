n = int(input())
for i in range(1,n+1):
    number = int(input())
    c=1

    if number ==1:
        print(f'#{i} 1')
        continue
    for j in range(2,number+1):
        if (j%2==0):
            c-=j
        else :
            c+=j
        
    print(f'#{i} {c}')

