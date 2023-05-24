from d15 import play
import pytest

test_input = {
    2020: [
        ([9, 19, 1, 6, 0, 5, 4], 1522),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
    ]
}
test_params = [(k, *i) for k, v in test_input.items() for i in v]


@pytest.mark.parametrize("turn,input_sn,expected", test_params)
def test_d15(turn, input_sn, expected):

    assert play(input_sn, turn) == f"{input_sn} - {turn}: {expected}"
