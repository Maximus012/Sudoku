import tkinter as tk


def input():
    values = []
    for row in range(9):
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

    if not valid_numbers:
        root.quit()
        instruction = tk.Label(root, text="Niepoprawne dane wejściowe. Spróbuj ponownie:", fg="red")
        instruction.grid(row=0, column=0, columnspan=9, padx=5, pady=5)
        root.mainloop()

    root.quit()
    return values


def invalid(value):
    if if_int(value):
        if if_digit(value):
            return False
    return True


def if_int(value):
    return str(value).isdigit()


def if_digit(value):
    if 1 <= int(value) <= 9:
        return True
    return False


invalid_numbers = False

root = tk.Tk()
root.title("Sudoku")

instruction = tk.Label(root, text="Wprowadź cyfry:")
instruction.grid(row=0, column=0, columnspan=9, padx=5, pady=5)

entries = []
for row in range(9):
    row_entries = []
    for column in range(9):
        entry = tk.Entry(root, width=3)
        entry.grid(row=row + 1, column=column, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

button = tk.Button(root, text="Potwierdź", command=input)
button.grid(row=10, column=0, columnspan=9, padx=5, pady=5)

root.mainloop()
