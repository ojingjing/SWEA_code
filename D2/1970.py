money = {
    50000 : 0 ,10000 :0 ,5000 :0 ,1000:0 , 500:0,100:0,50:0,10:0
}

n = int(input())

for q in range(n):
    m = int(input())

    
    for i in money:
            
        money[i] = m // i
        m = m % i

     
    print("#"+str(q+1))
    for j in money :
        
        print(money[j] , end=" ") 
    print()