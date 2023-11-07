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
            


def is_valid_sudoku(board):
    # 가로 검사
    for row in board:
        if not is_valid_row(row):
            return False
    
    # 세로 검사
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_row(column):
            return False
    
    # 3x3 작은 격자 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
            if not is_valid_row(square):
                return False
    
    return True

def is_valid_row(row):
    # 중복된 숫자가 없는지 확인
    seen = set()
    for num in row:
        if num != 0:
            if num in seen:
                return False
            seen.add(num)
    return True

# 테스트 케이스
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if is_valid_sudoku(board):
    print("1")  # 스도쿠 퍼즐이 올바르게 완성됨
else:
    print("0")  # 스도쿠 퍼즐에 중복된 숫자가 있음
