import pytest
from app.game import generate_table, CONST_TABLE_SIZE


class TestTable:
    def test_generate_table_rows_amount(self):
        table = generate_table()
        assert len(table) == CONST_TABLE_SIZE, "wrong table rows amount"

    def test_generate_table_columns_amount(self):
        table = generate_table()

        len_set = set()
        for row in table:
            len_set.add(len(row))

        assert len(len_set) == 1, "wrong cells amount in a table row"
        assert len_set.pop() == CONST_TABLE_SIZE, "wrong cells amount in a table row"

    def test_generate_table_cells_value(self):
        table = generate_table()

        values_set = set()
        for row in table:
            for cell in row:
                values_set.add(cell)

        values_list = list(values_set)
        values_list.sort()

        assert len(values_list) in [1, 2], "invalid amount of different value"
        assert values_list in [[0, 1], [0], [1]], "invalid value in one of the cells or missing values"
