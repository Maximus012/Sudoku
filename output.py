import tkinter as tk


def output(board):
    root = tk.Tk()
    root.title("Rozwiązanie")

    instruction = tk.Label(root, text="Rozwiązanie:")
    instruction.grid(row=0, column=0, columnspan=9, padx=5, pady=5)

    for row in range(9):
        for column in range(9):
            result = tk.Label(root, text=board[row][column], bg="white", width=2)
            result.grid(row=row + 1, column=column, padx=5, pady=5)

    button = tk.Button(root, text="Zakończ", command=root.destroy)
    button.grid(row=10, column=0, columnspan=9, padx=5, pady=5)

    root.mainloop()
