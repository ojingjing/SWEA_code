from collections import Counter
# n = int(input())

board = [list(map(int,input().split())) for _ in range(9)]
check =[[0 for _ in range(9)]for _ in range(9)]
for i in range (9):
    for j in range(9):
        check[i][j] = board[i][j]
        if j == 8 :
            print(Counter(check))
            # if counter.values == 1:
            #     print("ok")
            
