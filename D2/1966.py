t = int(input())

for i in range(t):
    n = int(input())
    number = list(map(int, input().split()))
    print(f'#{i+1} {" ".join(map(str, sorted(number)))}')