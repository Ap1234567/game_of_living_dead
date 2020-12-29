from app.game import get_next_gen_table


class TestGen:
    def test_survival(self, mock_table_for_tests, mock_parsed_rule):
        born_rule, survive_rule = mock_parsed_rule
        new_table = get_next_gen_table(mock_table_for_tests, born_rule, survive_rule)

        assert new_table[0][1] == 1
