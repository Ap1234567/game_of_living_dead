import pytest
from app.game import CONST_TABLE_SIZE


# fixture table format: (minimized)
# before:
#     0 1 0 1 0 0 0 0 0 0
#     1 1 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0

# after 1 gen:
#     1 1 0 0 0 0 0 0 0 0
#     1 1 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0
#     0 0 0 0 0 0 0 0 0 0

# cells to assert:
#   born - table[0][0]
#   staying alive - table[0][1]
#   staying dead - table [0][2]
#   die - table[0][3]

@pytest.fixture
def mock_table_for_tests():
    table = []
    for i in range(CONST_TABLE_SIZE):
        row = []
        for j in range(CONST_TABLE_SIZE):
            row.append(0)
        table.append(row)

    cells_to_resurrect = [
        # first row
        {"row": 0, "col": 0},
        {"row": 0, "col": 3},
        {"row": 0, "col": -2},
        # second row
        {"row": 1, "col": 0},
        {"row": 1, "col": 1},
        {"row": 1, "col": -2},
        {"row": 1, "col": -1},
    ]

    for cell in cells_to_resurrect:
        table[cell["row"]][cell["col"]] = 1

    return table

@pytest.fixture
def mock_parsed_rule():
    return [3], [2, 3]
