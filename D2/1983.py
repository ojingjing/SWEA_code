t = int(input())
grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for i in range(t):
    n , k = map(int,input().split())
    score =[]
    for j in range(n):
        a,b,c = map(int, input().split())
        score.append(a*0.35 + b*0.45 + c*0.2)
    kscore = score[k-1]
    score=sorted(score , reverse=True)
    print(score)
    kposition = score.index(kscore)
    print(kposition)
    srange = ((kposition)*(n //10))%10
    print(srange)
    print(f'#{i+1} {grade[srange]}')