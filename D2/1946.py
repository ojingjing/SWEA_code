t = int(input())
for q in range (t):
    n = int(input())
    save = []
    for i in range(n):
        english , count = map(str, input().split())
        for j in range(int(count)):
            save.append(english.upper())

    print(f'#{q+1}')
    for i in range(0, len(save),10):
        print(*save[i:i+10],sep='')