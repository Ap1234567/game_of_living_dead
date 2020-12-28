import random


# rule format: B3/S23 . B stand for born. S stand for survived.
def game_of_life(rule="B3/S23"):
    born_options, survived_options = parse_rule(rule)
    table = generate_table()
    print_table(table)


def parse_rule(rule):
    born_raw, survived_raw = rule.split("/")
    born_options = [int(x) for x in born_raw[1:]]
    survived_options = [int(x) for x in survived_raw[1:]]
    return born_options, survived_options


def generate_table():
    table = [[0] * 50] * 50

    amount_of_cells_to_live = random.randint(1, 50)
    for i in range(amount_of_cells_to_live):
        row = random.randint(0, 49)
        cell = random.randint(0, 49)
        table[row][cell] = 1

    return table


def print_table(table):
    for row in table:
        print(row)


if __name__ == '__main__':
    game_of_life("B3/S23")
