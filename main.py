from input import input
from solving import solving
from output import output

if __name__ == '__main__':
    board = input()
    print(board)
    board = solving(board)
    board = output(board)
