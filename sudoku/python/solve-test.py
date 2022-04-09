import pytest

from solve import get_row_col_for_sub_square


@pytest.mark.parametrize(
    "grid, sub_square_id, sub_square_index, expected_row, expected_col",
    [
        ([[], [], [], []], 0, 0, 0, 0),
        ([[], [], [], []], 1, 0, 0, 2),
        ([[], [], [], []], 2, 0, 2, 0),
        ([[], [], []], 0, 0, 0, 0),
    ],
)
def test_get_row_col_for_sub_square(
    grid, sub_square_id, sub_square_index, expected_row, expected_col
):

    row, col = get_row_col_for_sub_square(grid, sub_square_id, sub_square_index)

    assert row == expected_row
    assert col == expected_col
