n = int(input())

for i in range(1,n+1):
    count =0
    i=str(i)
    for j in i:
        if j in "369":
            count +=1
    if count ==0:
        print(i, end = " ")
    else:
        print("-"*count, end =" ")   




