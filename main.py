from input import input
from solving import solving
from output import output

if __name__ == '__main__':
    board = input()
    # board = solving(board)
    # tutaj board zmienia się na rozwiązaną, jak na razie nie ma solving(), więc po prostu przepisuje
    output(board)
