from input import input
from solving import solving
from output import output

if __name__ == '__main__':
    board = [[0 for a in range(9)] for b in range(9)]
    board = input(board)
    board = solving(board)
    board = output(board)
