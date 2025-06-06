import random

def generate_maze():
    puzzle = [
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
    return puzzle

def isvalid(board,row,col,num):
    for i in range(9):
        if board[row][i]==num or board[i][col]==num:
            return False
    
    start, end = 3*(row//3),3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start+i][end+j]==num:
                return False
    return True

def solve_sudoku_board(board,):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                for num in range(1,10):
                    if isvalid(board,row,col,num):
                        board[row][col]=num
                        if solve_sudoku_board(board):
                            return True
                        board[row][col]=0
                return False
    return True
            

     