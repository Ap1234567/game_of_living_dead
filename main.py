import random
import time
from termcolor import colored


# rule format: B3/S23 . B stand for born. S stand for survived.
def game_of_life(rule="B3/S23"):
    born_options, survived_options = parse_rule(rule)
    table = generate_table()

    while True:
        print_table(table)
        table = get_next_gen_table(table, born_options, survived_options)
        time.sleep(2)


def parse_rule(rule):
    born_raw, survived_raw = rule.split("/")
    born_options = [int(x) for x in born_raw[1:]]
    survived_options = [int(x) for x in survived_raw[1:]]
    return born_options, survived_options


def generate_table():
    table = []
    for i in range(50):
        row = []
        for j in range(50):
            row.append(0)
        table.append(row)

    amount_of_cells_to_live = random.randint(1, 2500)
    for i in range(amount_of_cells_to_live):
        row = random.randint(0, 49)
        cell = random.randint(0, 49)
        table[row][cell] = 1

    return table


def print_table(table):
    for row in table:
        for cell in row:
            if cell == 1:
                print(f"{colored(cell, 'green')} | ", end='')
            else:
                print(f"{colored(cell, 'red')} | ", end='')
        print()


def get_next_gen_table(old_table, born_options, survived_options):
    new_table = old_table.copy()
    for row_index, row in enumerate(old_table):
        for column_index, cell in enumerate(row):
            surrounding_cells = get_surrounding_cells_list(old_table, row_index, column_index)
            new_table[row_index][column_index] = get_new_cell_value(cell, surrounding_cells, born_options, survived_options)

    return new_table


def get_surrounding_cells_list(table, row_index, column_index):
    cells_list = []
    relevant_rows = [row_index - 1, row_index, row_index + 1]
    relevant_columns = [column_index - 1, column_index, column_index + 1]

    for row in relevant_rows:
        if row < 0 or 49 < row:
            continue
        for column in relevant_columns:
            # do not add the cell itself
            if column < 0 or 49 < column:
                continue
            if row == row_index and column == column_index:
                continue
            cells_list.append(table[row][column])

    return cells_list


def get_new_cell_value(existing_cell_value, surrounding_cells, born_options, survived_options):
    amount_of_living_surroundings = sum([x for x in surrounding_cells if x == 1])
    if existing_cell_value == 1:
        if amount_of_living_surroundings in survived_options:
            return 1
        return 0
    if amount_of_living_surroundings in born_options:
        return 1
    return 0


if __name__ == '__main__':
    game_of_life("B3/S23")
