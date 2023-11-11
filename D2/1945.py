t = int(input())

for q in range(t):

    so = {2:0,3:0,5:0,7:0,11:0}

    n = int(input())

    for key in so :
        while n >1 and n % key ==0 :
            n = n // key 
            so[key] +=1

    print(f'#{q+1} {" ".join(map(str,so.values()))}')
