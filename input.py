import tkinter as tk


def input():
    root = tk.Tk()
    root.title("Sudoku")

    instruction = tk.Label(root, text="Wprowadź cyfry:")
    instruction.grid(row=0, column=0, columnspan=11, padx=5, pady=5)

    entries = []
    for row in range(11):
        row_entries = []
        for column in range(11):
            if row in (3, 7):
                separator_row = tk.Frame(root, height=1, bg="black")
                separator_row.grid(row=row + 1, column=column, columnspan=1, sticky="ew")
            elif column in (3, 7):
                separator_column = tk.Frame(root, width=1, bg="black")
                separator_column.grid(row=row + 1, column=column, rowspan=1, sticky="ns")
            else:
                entry = tk.Entry(root, width=3)
                entry.grid(row=row + 1, column=column, padx=5, pady=5)
                row_entries.append(entry)

        entries.append(row_entries)

    button = tk.Button(root, text="Potwierdź", command=root.quit)
    button.grid(row=12, column=0, columnspan=11, padx=5, pady=5)

    root.mainloop()
    return get_values(root, entries, instruction)


def get_values(root, entries, instruction):
    correct_range = [0, 1, 2, 4, 5, 6, 8, 9, 10]
    while True:
        values = []
        for row in correct_range:
            row_values = []
            for column in range(9):
                row_values.append((entries[row][column].get()).strip())
            values.append(row_values)

        valid_numbers = True
        for row in range(9):
            for column in range(9):
                if values[row][column] != '' and invalid(values[row][column]):
                    valid_numbers = False
                    break

        if valid_numbers:
            break
        else:
            error(root, instruction)

    root.destroy()
    return values


def error(root, instruction):
    root.quit()
    instruction.config(text="Niepoprawne dane wejściowe. Spróbuj ponownie.", fg="red")
    root.mainloop()


def invalid(value):
    if if_integer(value):
        if if_digit(value):
            return False
    return True


def if_integer(value):
    return str(value).isdigit()


def if_digit(value):
    if 1 <= int(value) <= 9:
        return True
    return False
