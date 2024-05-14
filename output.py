import tkinter as tk


def output(board):
    root = tk.Tk()
    root.title("Rozwiązanie")

    instruction = tk.Label(root, text="Rozwiązanie:")
    instruction.grid(row=0, column=0, columnspan=11, padx=5, pady=5)

    row_correction = 0
    for row in range(11):
        column_correction = 0
        if row in (3, 7):
            row_correction += 1
        for column in range(11):
            if row in (3, 7):
                separator_row = tk.Frame(root, height=1, bg="black")
                separator_row.grid(row=row + 1, column=column, columnspan=1, sticky="ew")
            elif column in (3, 7):
                separator_column = tk.Frame(root, width=1, bg="black")
                separator_column.grid(row=row + 1, column=column, rowspan=1, sticky="ns")
                column_correction += 1
            else:
                result = tk.Label(root, text=board[row - row_correction][column - column_correction], bg="white", width=2)
                result.grid(row=row + 1, column=column, padx=5, pady=5)

    button = tk.Button(root, text="Zakończ", command=root.destroy)
    button.grid(row=12, column=0, columnspan=11, padx=5, pady=5)

    root.mainloop()
