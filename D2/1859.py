from collections import deque
n= int(input())

for i in range(1,n+1):
    m = int(input())
    l =deque(map(int, input().split()))
    count =0
    maxcount = max(l)

    if l[0] == maxcount:
        print("#"+"1"+" "+"0")
        continue
       
    for _ in range(m-1):

        if l[0] <maxcount :
            count += maxcount-l.popleft()
        
        elif l[0] == maxcount :
            l.popleft()
            maxcount = max(l)
    print("#"+str(i)+" "+str(count))
