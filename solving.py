def solving(board):
    board = char_to_num(board)
    if solve_board(board):
        return num_to_char(board)
    else:
        return None


def solve_board(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                for num in range(1, 10):
                    if if_digit_correct(board, row, column, num):
                        board[row][column] = num
                        if solve_board(board):
                            return True
                        board[row][column] = 0
                return False
    return True


def if_digit_correct(board, row, column, num):
    if row_correct(board, row, num):
        if column_correct(board, column, num):
            if area_correct(board, row, column, num):
                return True
    return False


def row_correct(board, row, num):
    for column in range(9):
        if board[row][column] == num:
            return False
    return True


def column_correct(board, column, num):
    for row in range(9):
        if board[row][column] == num:
            return False
    return True


def area_correct(board, row, column, num):
    start_row = row - row % 3
    start_column = column - column % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_column + j] == num:
                return False
    return True


def char_to_num(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == '':
                board[row][column] = 0
            else:
                board[row][column] = int(board[row][column])
    return board


def num_to_char(board):
    for row in range(9):
        for column in range(9):
            board[row][column] = str(board[row][column])
    return board
