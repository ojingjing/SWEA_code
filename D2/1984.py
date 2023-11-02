n =int(input())

for i in range(n):
    bag = list(map(int, input().split()))
    bag.remove(max(bag))
    bag.remove(min(bag))
    print(f'#{i+1} {round(sum(bag)/len(bag))} ')
